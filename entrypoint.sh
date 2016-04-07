#!/bin/bash

forever start --debug --verbose  --watch --watch --watchDirectory /src/cv.soulshake/net/server/ --append -l out.log server.js
forever logs -f server.js
