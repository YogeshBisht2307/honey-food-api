# Honey Food Setup

## Authenticate docker with artifact repository
```
    gcloud auth configure-docker asia-south1-docker.pkg.dev

```


## Run cloud run locally using docker
```
    docker run -p 80:80 \
        --env-file .env \
        -v "$HOME/.config/gcloud/application_default_credentials.json":/gcp/creds.json:ro \
        --name honey-food \
        kodeweich/honey-food

```


## Tag Docker Images
```
    docker tag kodeweich/honey-food asia-south1-docker.pkg.dev/cloud-kota/honey-food/honey-food

```

## Untag Docker Images
```
    gcloud artifacts docker tags delete asia-south1-docker.pkg.dev/cloud-kota/honey-food/honey-food:latest
```

## Push docker image to artifact repository

```
    docker push asia-south1-docker.pkg.dev/cloud-kota/honey-food/honey-food:latest
```


##  API Access

https://honey-food-2k4fxbvuna-el.a.run.app/api/v1/docs

X-HONEY-FOOD-API-KEY : "NAkJDX7YhjV4zLJG6y87mHKdM6NhJgwoujwwb5fI"