docker build -t arthurv1/weather-api:1.0.0 .
docker run -p 3000:3000 arthurv1/weather-api:1.0.0
docker tag arthurv1/weather-api:1.0.0 arthurv1/weather-api:latest  
docker push arthurv1/weather-api:latest