FROM node
MAINTAINER AJ Bowen <aj@soulshake.net>

RUN apt-get update && apt-get install -y git
RUN npm install -g forever

RUN mkdir /src
COPY . /src/cv.soulshake.net
WORKDIR /src/cv.soulshake.net
RUN npm install

WORKDIR /src/cv.soulshake.net/server
EXPOSE 1337
ENTRYPOINT ["../entrypoint.sh"]
