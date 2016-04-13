# My CV

This repo contains the source code and Dockerfile for [cv.soulshake.net](cv.soulshake.net).

It serves a command-line version of my resume using [wopr](https://github.com/yaronn/wopr), node.js, Docker and the Docker Cloud.

To view it, run:

`````bash
$> curl -N cv.soulshake.net/?cols=$((COLUMNS))&rows=$((LINES))&terminal=${TERM}

`````

## Tips

    * Maximize the terminal before viewing the report for best viewing experience  
    * If you <kbd>CTRL+C</kbd> in the middle or rendering your cursor might disappear. Restore it by running again and letting the render complete or with `$> echo '\033[?25h'`
    * Disable curl buffering with the -N flag.

Created by AJ Bowen ([@s0ulshake](https://twitter.com/s0ulshake))

