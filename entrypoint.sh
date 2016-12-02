#!/bin/bash

# in wopr/server/server.js, this line is hardcoded:
# var content = fs.readFileSync(__dirname+'/../examples/sample.xml')
# So, replace the filename with our own
OUR_FILE="/data/resume.xml"
sed -i "s;__dirname+'/../examples/sample.xml';'$OUR_FILE';" /wopr/server/server.js

# Same thing with this line:
# res.writeHead(301, {'Location': 'https://github.com/yaronn/wopr'});
OUR_URL="http://blog.soulshake.net/2016/04/command-line-resume/"
sed -i "s;__dirname+'https://github.com/yaronn/wopr';'$OUR_URL';" /wopr/server/server.js

forever start --debug --verbose  --watch --watchDirectory /data --fifo server.js --port "80"
forever logs -f server.js
