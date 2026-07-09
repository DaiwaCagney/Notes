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
- `oc get dc -n <namespace>`
- `oc rollout history dc/<deployment config> -n <namespace>`
- `oc scale dc/<deployment config> --replicas=0`
- `oc apply -f debug-ubi.yaml`
- `oc rsh debug-ubi`
- `oc delete pod debug-ubi`
- `oc delete -f debug-ubi.yaml`

## Debug Pod
```
apiVersion: v1
kind: Pod
metadata:
  name: debug-ubi
spec:
  restartPolicy: Never
  containers:
    - name: debug
      image: registry.access.redhat.com/ubi9/ubi
      command: ["sleep", "3600"]
      resources:
        requests:
          cpu: "50m"
          memory: "64Mi"
        limits:
          cpu: "200m"
          memory: "256Mi"
      volumeMounts:
        - name: data
          mountPath: /mnt/data
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: <pvc claim>
```
