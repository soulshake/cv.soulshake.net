#!/bin/bash

forever start --debug --verbose  --watch --watch --watchDirectory /src/wopr/server/ --append -l out.log server.js
forever logs -f server.js
