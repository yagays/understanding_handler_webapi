# understanding_handler_webapi

[Flask/FastAPIライクなルーティングとパスパラメータの仕組みを、単純な実装から理解する](https://zenn.dev/yag_ays/articles/4a91622bbfc83c)

## Install

```sh
$ poetry install
```

## Run
### Step 1

```
$ poetry run gunicorn app_1:app
```

### Step 2

```
$ poetry run gunicorn app_2:app
```

### Step 3

```
$ poetry run gunicorn app_3:app
```

## Endpoint

- [http://127.0.0.1:8000/home](http://127.0.0.1:8000/home)
- [http://127.0.0.1:8000/hello/yag](http://127.0.0.1:8000/hello/yag)
- [http://127.0.0.1:8000/not_found](http://127.0.0.1:8000/not_found)