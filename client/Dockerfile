# Build the image with:
# docker build -t wopr-client .
FROM alpine:latest
MAINTAINER AJ Bowen <aj@soulshake.net>

RUN apk add --update curl
#ENTRYPOINT ["$@"]
#CMD ["/usr/bin/curl","-N"]
#,"localhost:1337/\[0-2\]\?auto\&cols=$((COLUMNS))"]
#ENTRYPOINT ["/usr/bin/curl", "-N"]

# Run the container with:
# docker run --rm --name wopr-client -ti --net container:wopr-server \
#     -e COLUMNS=$COLUMNS -e LINES=$LINES \
#     wopr-client curl -N localhost:1337/\[0-2\]\?auto\&cols=$((COLUMNS))
