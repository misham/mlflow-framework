# Setup MLFlow-based framework

Reference [Aporia blog post](https://www.aporia.com/blog/building-an-ml-platform-from-scratch/) for more info.

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
