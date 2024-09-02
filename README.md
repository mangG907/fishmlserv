# fishmlserv

## Deploy

![image](https://github.com/user-attachments/assets/2cc17eec-a366-41e7-bddd-4f55ce1abb2b)

### Run
- dev
- http://localhost:8000//docs
```bash
# uvicorn --help
$ uvicorn src.fishmlserv.main:app --reload
```

- prd
```bash
$ uvicorn src.fishmlserv.main:app --host 0.0.0.0 --port 8949
```

### Docker
```bash
$ sudo docker build -t fishmlserv:0.4.0 .
$ sudo docker run -d --name fmlserv-040 -p 8877:8765 fishmlserv:0.4.0
```

### Fly.io
```
$ fly launch --no-deploy
$ flyctl launch --name mariofish
$ flyctl scale memory 256
$ flyctl deploy
```

### Ref
- https://curlconverter.com/python
