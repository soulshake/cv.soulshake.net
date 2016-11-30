FROM node
MAINTAINER AJ Bowen <aj@soulshake.net>

RUN apt-get update && apt-get install -y git
RUN npm install -g forever

RUN git clone https://github.com/yaronn/wopr.git
WORKDIR /wopr
RUN npm install

EXPOSE 1337
EXPOSE 80

COPY entrypoint.sh /entrypoint.sh

# Some envvars are needed to correctly render the graphics
ENV LANG=en_US.utf8
ENV TERM=xterm-256color

# Copy /data directory; this can also be mounted at runtime and changes will be reloaded live
COPY data /data

WORKDIR /wopr/server
ENTRYPOINT /entrypoint.sh
