# The very professional Curriculum Vitae of AJ Bowen

[![Build Status](https://travis-ci.org/soulshake/cv.soulshake.net.svg?branch=master)](https://travis-ci.org/soulshake/cv.soulshake.net)

This repo contains the source code and Dockerfile for [cv.soulshake.net](http://cv.soulshake.net).

It serves a command-line version of my resume using [wopr](https://github.com/yaronn/wopr), node.js, Docker and Swarm.

To view it, run:

`````bash
curl cv.soulshake.net
`````

## Tips

  * Maximize the terminal before viewing the report for best viewing experience
  * If you <kbd>CTRL+C</kbd> in the middle or rendering your cursor might disappear. Restore it by running again and letting the render complete or with `$> echo '\033[?25h'`
  * Disable curl buffering with the -N flag.

Created by AJ Bowen ([@s0ulshake](https://twitter.com/s0ulshake)). For details, see [this blog post](http://blog.soulshake.net/2016/04/command-line-resume/).
