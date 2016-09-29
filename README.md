# My CV

This repo contains the source code and Dockerfile for [cv.soulshake.net](http://cv.soulshake.net).

It serves a command-line version of my resume using [wopr](https://github.com/yaronn/wopr), node.js, Docker and the Docker Cloud.

To view all slides, run:

`````bash
p=0; while [ $p -lt 9 ]; do curl -N cv.soulshake.net/$((p++)); read; done
`````

To view a specific slide, run:

`````bash
curl -N cv.soulshake/3/
`````

If the slides don't display correctly, try including URL parameters `cols`, `rows` or `terminal`:

`````bash
$> curl -N cv.soulshake.net/?cols=$((COLUMNS))&rows=$((LINES))&terminal=${TERM}
`````

## Tips

  * Maximize the terminal before viewing the report for best viewing experience  
  * If you <kbd>CTRL+C</kbd> in the middle or rendering your cursor might disappear. Restore it by running again and letting the render complete or with `$> echo '\033[?25h'`
  * Disable curl buffering with the -N flag.

Created by AJ Bowen ([@s0ulshake](https://twitter.com/s0ulshake)). For details, see [this blog post](http://blog.soulshake.net/2016/04/command-line-resume/).
