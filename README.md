## Configuration values for ArgoCD managed repository

## ArgoCD UI

Please "Log in via SAML"

```shell
https://argocd.devops.transcendplatform.com/
```


### Root directory structure

- README.md 
- Tenant names 
- globalValues.yaml - Global values for all tenants and enviroments.

```shell
.
├── README.md
├── devops
├── fs
├── globalValues.yaml
├── sndbx
└── trn

```
### Tenant directory

- clientValues.yaml - Values for all environments in specific tenant
- environments list

```shell
.
├── clientValues.yaml
└── dev
```

### Environment directory

- environmentValues.yaml - environment specific values for all microservices
- infra directory - environment specific values for third-party services
- infrastructure.yaml - list of third-party services
- microservices directory - environment specific values for microservices
- microservices.yaml - list of microservices
- rootApp - ArgoCD template application for microservices and infrastructure. 
```shell

.
├── environmentValues.yaml
├── exceptions.yaml
├── infra
│   ├── cert-manager
│   │   └── applicationValues.yaml
│   ├── cert-manager-resources
│   │   └── applicationValues.yaml
│   ├── grafana
│   │   └── applicationValues.yaml
│   ├── ingress-azure
│   │   └── applicationValues.yaml
│   └── secret-provider-class
│       └── applicationValues.yaml
├── infrastructure.yaml
├── microservices
│   ├── card-pin
│   │   └── applicationValues.yaml
│   ├── client-credentials
│   │   └── applicationValues.yaml
│   ├── dlq-processor
│   │   └── applicationValues.yaml
│   ├── employee-service
│   │   └── applicationValues.yaml
│   ├── fps-store-config
│   │   └── applicationValues.yaml
│   ├── fulfilment
│   │   └── applicationValues.yaml
│   ├── fulfilment-order-processor
│   │   └── applicationValues.yaml
│   ├── fulfilment-order-processor-grouping-cronjob
│   │   └── applicationValues.yaml
│   ├── fulfilment-order-processor-scheduler-cronjob
│   │   └── applicationValues.yaml
│   ├── gravity
│   │   └── applicationValues.yaml
│   ├── identity-config
│   │   └── applicationValues.yaml
│   ├── issue-token
│   │   └── applicationValues.yaml
│   ├── labelprintingservice
│   │   └── applicationValues.yaml
│   ├── loading-service
│   │   └── applicationValues.yaml
│   ├── luservice
│   │   └── applicationValues.yaml
│   ├── luservice-sync-cronjob
│   │   └── applicationValues.yaml
│   ├── mockserver
│   │   └── applicationValues.yaml
│   ├── mountebank
│   │   └── applicationValues.yaml
│   ├── ods
│   │   └── applicationValues.yaml
│   ├── order-adapter
│   │   └── applicationValues.yaml
│   ├── pickadmin
│   │   └── applicationValues.yaml
│   ├── pickingservice
│   │   └── applicationValues.yaml
│   ├── pickingservice-buffer-check-cronjob
│   │   └── applicationValues.yaml
│   ├── printing-adapter
│   │   └── applicationValues.yaml
│   ├── prodprojservice
│   │   └── applicationValues.yaml
│   ├── prodprojservice-buffer-sync-cronjob
│   │   └── applicationValues.yaml
│   ├── product-adapter
│   │   └── applicationValues.yaml
│   ├── reports-service
│   │   └── applicationValues.yaml
│   ├── secure-http-requests-cronjob
│   │   └── applicationValues.yaml
│   ├── token-exchange
│   │   └── applicationValues.yaml
│   ├── webhook-delivery-service
│   │   └── applicationValues.yaml
│   └── webhook-delivery-service-retry-cronjob
│       └── applicationValues.yaml
├── microservices.yaml
└── rootApp
    ├── Chart.yaml
    ├── README.md
    ├── templates
    │   ├── infrastructure.yaml
    │   └── microservices.yaml
    └── values.yaml


```

## How to

### Add new microservice

- Navigate to tenant/environment_name 
- Add microservice to microservices.yaml file
- Create directory tenant/environment_name/microservices/my-new-microservice
- Create tenant/environment_name/microservices/my-new-microservice/applicationValues.yaml
- (Optional) Add any specific microservice values to tenant/environment_name/microservices/my-new-microservice/applicationValues.yaml

### Add new third-party

- Navigate to tenant/environment_name
- Add third-party application to infrastructure.yaml file
- Create directory tenant/environment_name/infra/my-new-third-party-application
- Create tenant/environment_name/infra/my-new-third-party-application/applicationValues.yaml
- (Optional) Add any specific values to tenant/environment_name/infra/my-new-third-party-application/applicationValues.yaml
