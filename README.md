All commands must be run from top level directory

### Running the Container
docker build -t folio-server .
docker run -d --name server1 -p 3000:80 folio-server

### Running the app locally

```
uvicorn application.src.main:app --host 0.0.0.0 --port 80
```

### Running unit tests
```
pytest
```

### Adding Tables or Procedures to Database
Create the necessary SQL files in its corresponding directory
Run the following from the top level directory:

```
python application/src/dal/setup.py
```

This will iterate through both the tables and procedures directories and execute the SQL files contained within them.