#!/bin/bash

# in wopr/server/server.js, this line is hardcoded:
# var content = fs.readFileSync(__dirname+'/../examples/sample.xml')
# So, replace the filename with our own
OUR_FILE="/data/resume.xml"
sed -i "s;__dirname+'/../examples/sample.xml';'$OUR_FILE';" /wopr/server/server.js

forever start --debug --verbose  --watch --watchDirectory /data --fifo server.js --port "80"
#forever start --debug --verbose  --watch --watchDirectory /data --append -l out.log server.js
forever logs -f server.js
