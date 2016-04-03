FROM node
MAINTAINER AJ Bowen <aj@soulshake.net>

RUN apt-get update && apt-get install -y git
RUN npm install -g forever

RUN mkdir /src
WORKDIR /src
RUN git clone https://github.com/soulshake/cv.soulshake.net.git
WORKDIR /src/wopr
RUN npm install

WORKDIR /src/wopr/server
EXPOSE 1337
ENTRYPOINT ["../entrypoint.sh"]
