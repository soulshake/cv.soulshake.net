# Build image with:
# docker build -t wopr .
FROM node
MAINTAINER AJ Bowen <aj@soulshake.net>

RUN apt-get update && apt-get install -y git
RUN npm install -g forever

RUN mkdir /src
RUN git clone https://github.com/yaronn/wopr.git /src/wopr
WORKDIR /src/wopr
RUN npm install \
    blessed@0.1.7 \
    blessed-contrib@2.3.1 \
    xml2js@0.4.9

WORKDIR /src/wopr/server

# Launch container with:
# docker run --rm --name wopr-server -ti --publish-all --entrypoint bash wopr

# Within the container, run:
# forever start -l forever.log server.js
# forever logs -f server.js
