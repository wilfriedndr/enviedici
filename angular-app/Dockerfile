# Étape 1 : build Angular
FROM node:20 AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build -- --configuration production --base-href=/app/ --deploy-url=/app/ --project enviedici-app

# Étape 2 : image Nginx
FROM nginx:stable-alpine
COPY --from=builder /app/dist/enviedici-app/browser /usr/share/nginx/html/app
COPY nginx.conf /etc/nginx/conf.d/default.conf
