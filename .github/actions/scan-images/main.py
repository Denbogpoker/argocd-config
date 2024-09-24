import os
import sys
from ruamel.yaml import YAML
from subprocess import run

subscriptions_directory = "."
all_subscriptions = ["trn", "fs"]
all_environments = ["dev", "stg", "prod"]
yaml = YAML()


def run_snyk(command: str):
    d = dict(os.environ)
    result = run(command, shell=True, capture_output=True, env=d)
    if result.returncode:
        raise Exception(
            f"Command: {command}, returned exit code: {result.returncode} & stderr: {result.stderr} & stdout: {result.stdout}")
    return result.stdout


def get_applications(subscription_path: str, environment_path: str):
    file_path = f'{subscriptions_directory}/{subscription_path}/{environment_path}/microservices.yaml'
    if os.path.exists(file_path):
        with open(file_path) as f:
            return yaml.load(f)['microservices']
    return []


def scan_application(application, snyk_project: str):
    if 'chart' in application:
        name = application['name']
        image_tag = application['version']
        repository = application['chart']
        registry = application['applicationRepositoryUrl']
        print(f'helm pull oci://{registry}/{repository} --version {image_tag} --untar --untardir ./{snyk_project}')
        run_snyk(f'helm pull oci://{registry}/{repository} --version {image_tag} --untar --untardir ./{snyk_project}')
        helm_file_path = f'./{snyk_project}/{name}/values.yaml'
        if os.path.exists(helm_file_path):
            with open(helm_file_path) as f:
                image = yaml.load(f)['image']
                container_repository = image['repository']
                tag = image['tag']
                run_snyk(f'snyk container monitor {registry}/{container_repository}:{tag} --project-name={snyk_project}')


def scan_environment(subscription_in: str, environments_in: str, applications_in: str):
    microservices = get_applications(subscription_in, environments_in)
    for application in microservices:
        if applications_in == "all" or applications_in == application['name']:
            scan_application(application, f"{subscription_in}-{environments_in}")


def scan_subscription(subscription_in: str, environments_in: str, applications_in: str):
    if environments_in == "all":
        for environment in all_environments:
            scan_environment(subscription_in, environment, applications_in)
    else:
        scan_environment(subscription_in, environments_in, applications_in)


if __name__ == '__main__':
    subscriptions = sys.argv[1]
    environments = sys.argv[2]
    applications = sys.argv[3]
    if subscriptions == "all":
        for subscription in all_subscriptions:
            scan_subscription(subscription, environments, applications)
    else:
        scan_subscription(subscriptions, environments, applications)
