docker build -t arthurv1/stats-api:1.0.0
docker run -p 8080.8080 arthurv1/stats-api:1.0.0
docker push arthurv1/stats-api:1.0.0
docker build -t arthurv1/stats-api:2.0.0
docker run -p 8080:8080 arthurv1/stats-api:2.0.0
docker tag arthurv1/stats-api:2.0.0 arthurv1/stats-api:latest
docker push arthurv1/stats-api:latest
docker pull arthurv1/stats-api:2.0.0