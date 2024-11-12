FROM nginx:mainline
RUN rm -f /etc/nginx/conf.d/default.conf 
COPY jusan-dockerfile.conf /etc/nginx/conf.d/
COPY jusan-dockerfile/ /var/www/jusan-dockerfile
EXPOSE 6060
CMD ["nginx", "-g", "daemon off;"]