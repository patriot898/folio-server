### Running the Container
docker build -t folio-server .
docker run -d --name server1 -p 3000:80 folio-server
