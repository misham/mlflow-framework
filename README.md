# Setup MLFlow-based framework

Reference [Aporia blog post](https://www.aporia.com/blog/building-an-ml-platform-from-scratch/) for more info.

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
