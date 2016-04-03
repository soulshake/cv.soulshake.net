# My CV

This repo contains the source code and Dockerfile for [cv.soulshake.net](cv.soulshake.net).

It serves a command-line version of my resume using the excellent [wopr](https://github.com/yaronn/wopr), node.js, Docker and EC2.

WOPR is a simple markup language for creating [rich terminal reports](https://github.com/yaronn/blessed-contrib), presentations and infographics.

To view it, run:

`````bash
$> curl -N cv.soulshake.net:32769/?cols=$((COLUMNS))&rows=$((LINES))&terminal=${TERM}

`````

Created by AJ Bowen ([@s0ulshake](https://twitter.com/s0ulshake))


**Tip:** Maximize the terminal before viewing the report for best viewing experience  
**Tip:** If you <kbd>CTRL+C</kbd> in the middle or rendering your cursoe might disappear. Restore it by running again and letting the render complete or with `$> echo '\033[?25h'`


**Pages**

When viewing a report with the local viewer you can advance slides with the Return or Space keys.
When using the online viewer you have 2 options:

**Option 1:** Manually advance slides with Return or Space:

`````bash
p=0; while true; do curl tty.zone/$((p++))\?cols=$((COLUMNS)); read; done
`````

**Option 2:** Slides advance automatically every 5 seconds:

`````bash
curl -N tty.zone/\[0-2\]\?auto\&cols=$((COLUMNS))
`````

Where 0 is the index of the first slide and 2 of the last slide. Keep the brackets in the url (they are not to express optional argument) and escape them as in the above sample.

Tip: disable curl buffering with the -N flag

##License##
MIT


## More Information
Created by AJ Bowen ([twitter](http://twitter.com/s0ulshake), [blog](http://blog.soulshake.net/))
