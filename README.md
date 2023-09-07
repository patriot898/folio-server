### Running the Container
docker build -t folio-server .
docker run -d --name server1 -p 3000:80 folio-server

### Running the app locally
Run the following from the top level directory:

```
uvicorn application.src.main:app --host 0.0.0.0 --port 80
```
