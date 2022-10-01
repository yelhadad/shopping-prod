FROM nginx:latest
WORKDIR /client
COPY ./ ./
RUN rm -f /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf