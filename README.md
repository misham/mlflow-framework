# Setup MLFlow-based framework

Reference [Aporia blog post](https://www.aporia.com/blog/building-an-ml-platform-from-scratch/) for more info.

The goal is to build out a MLFlow with a basic model, storing the artifacts locally. This includes training a simplistic model and serving the results via FastAPI.

Instead of Kubernetes and AWS, this project uses Docker Compose and keeps everything locally. DVC remote storage is not used here, however, the data file is imported from the gist referenced in the article.

## Notes

This uses FTP container for storing artifacts. It takes over local port 21 for this purpose. If you have something running on port 21, please turn it off before starting up this "framework".

## Dependencies

### libomp

#### Mac

```shell
brew install libomp
```

## Running

```shell
poetry install
docker compose up -d
poetry run train
```

### Testing

The server is started on `http://localhost:8000` port. It expects a run ID from MLFlow UI in the path. The format for the requests is: `http://localhost:8000/<run ID>/`.
#### Sample data

```
Setosa: "{ 'sepal': { 'length': 4.9, 'width': 3.1 }, 'petal': { 'length': 1.5, 'width': 0.1 } }"
Virginica '{ "sepal": { "length": 6.8, "width": 3 }, "petal": { "length": 5.5, "width": 2.1 } }'
```

#### Setosa output
```shell
curl -X 'POST' 'http://localhost:8000/predict/<Run ID>' -H 'accept: application/json' -H 'Content-Type: application/json' \
  -d '{ "sepal": { "length": 4.9, "width": 3.1 }, "petal": { "length": 1.5, "width": 0.1 } }'
```

#### Virginica output
```shell
curl -X 'POST' 'http://localhost:8000/predict/<Run ID>' -H 'accept: application/json' -H 'Content-Type: application/json' \
  -d '{ "sepal": { "length": 6.8, "width": 3 }, "petal": { "length": 5.5, "width": 2.1 } }'
```