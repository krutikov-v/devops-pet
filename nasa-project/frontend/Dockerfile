FROM nginx:alpine

# Кладём свой конфиг nginx (с прокси /api -> backend:5000)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Кладём статическую страницу
COPY index.html /usr/share/nginx/html/index.html
