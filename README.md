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
