FROM node:10-alpine
RUN mkdir -p /run/nginx

COPY package.json package.json
RUN npm install


COPY . .

RUN npm install -g serve
RUN npm run build

FROM nginx:alpine
COPY /build/ /usr/share/nginx/html
EXPOSE 80


CMD ["nginx", "-g", "daemon off;"]

EXPOSE 3000
