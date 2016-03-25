FROM debian:jessie
MAINTAINER AJ Bowen <aj@soulshake.net>

RUN apt-get upgrade -y
RUN apt-get update

RUN apt-get install -y \
    curl \
    sudo

RUN echo "alias ll='ls -alhF'" >> $HOME/.bashrc

RUN curl -sL https://deb.nodesource.com/setup_5.x > setup
RUN sudo -E bash setup
RUN sudo apt-get install -y nodejs
RUN sudo npm install -g wopr
RUN sudo apt-get install -y \
    console-braille \
    git
WORKDIR /src
#RUN git clone https://github.com/yaronn/blessed-contrib.git
RUN git clone https://github.com/yaronn/wopr.git
COPY . /src
WORKDIR /src/wopr
RUN npm install
RUN ls node_modules
EXPOSE 1337
WORKDIR /src/wopr/server
ENTRYPOINT ["node", "server.js"]
