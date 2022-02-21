

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