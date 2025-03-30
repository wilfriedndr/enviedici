# Étape 1 : build de l'app Angular
FROM node:20 AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build --prod

# Étape 2 : NGINX pour servir le contenu
FROM nginx:stable-alpine

# Supprime la config par défaut
RUN rm -rf /usr/share/nginx/html/*

# Copie le build Angular vers nginx
COPY --from=builder /app/dist/enviedici-app/browser /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copie une config NGINX personnalisée si nécessaire
# COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
