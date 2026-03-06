docker build -t hello-flask:1.0.0 .
docker run -p 5000:5000 hello-flask:1.0.0
docker tag hello-flask:1.0.0 hello-flask:latest
docker images