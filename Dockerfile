FROM node
MAINTAINER AJ Bowen <aj@soulshake.net>

RUN apt-get update && apt-get install -y \
    git

RUN npm install -g forever

RUN mkdir /src
COPY package.json /src/cv.soulshake.net/package.json

WORKDIR /src/cv.soulshake.net
RUN npm install
COPY . /src/cv.soulshake.net
ENV VIRTUAL_HOST "cv.soulshake.net"
ENV LANG=en_US.utf8
ENV TERM=xterm-256color

WORKDIR /src/cv.soulshake.net/server
EXPOSE 1337
ENTRYPOINT ["../entrypoint.sh"]
