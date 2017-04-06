FROM node:boron

RUN npm install -g stubby

EXPOSE 7443 8882 8889

CMD ["stubby", "-d", "/tmp/stubby.yml", "-w"]
