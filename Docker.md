# Docker

## Docker
- `docker build -t test-image:latest .`
- `docker load -i test-image.tar`
- `docker save -o test-image.tar test-image:latest`
- `docker login -u <username> -p <token> <registry URL>`
- `docker tag test-image:latest <registry URL>/<namespace>/test-image:latest`
- `docker push <registry URL>/<namespace>/test-image:latest`
- `docker pull docker.io/sonarqube:25.1.0.102122-community`

## Docker Set Insecure Registry
```
{
  "builder": {
    "gc": {
      "defaultKeepStorage": "20GB",
      "enabled": true
    }
  },
  "experimental": false,
  "insecure-registries": [
    "YOUR-REGISTRY-URL-HERE"
  ]
}
```

## OC
- `oc login -u <username> <domain> --insecure-skip-tls-verify=true`
- `oc whoami -t`
- `oc registry info --public`
- `oc project -q`
- `oc project <namespace>`
- `oc -n <namespace> get istag`
- `oc get pods -n <namespace>`
