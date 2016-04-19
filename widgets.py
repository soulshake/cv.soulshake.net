#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import click
"""
This library is intended to generate XML suitable for being served by a wopr server.
# Error: no such widget: undefined --> forgot to specify item colSpan etc
"""

class Document:
    """
    A Document is a series of pages. Documents are structured as follows:

    <document>
        <page>
            <item col="n", row="n", colSpan="n", rowSpan="n">
                <WIDGET_TYPE>
                </WIDGET_TYPE>
            </item>
        </page>
    </document>
    """
    def __init__(self, pages):
        self.pages = pages

    @property
    def content(self):
        ret = []
        ret.append("<document>")
        for page in self.pages:
        #    print(self.pages[page].grid)
            ret.append(self.pages[page].content)
        ret.append("</document>")

        return "\n".join(ret)


class Page:
    """
    A page is a 12x12 grid in which you can position different widgets (within <item> tags).
    """
    def __init__(self):
        self.widgets = []

    def add_widget(self, widget):
        self.widgets.append(widget)

    @property
    def grid(self):
        ret = []
        for widget in self.widgets:
            ret.append(((widget.col, widget.row), (widget.colSpan, widget.rowSpan)))
        return ret

    @property
    def content(self):
        ret = []
        ret.append("<page>")
        for widget in self.widgets:
            ret.append(widget.content)
        ret.append("</page>")
        ret.append("")
        return "\n".join(ret)

class Widget(object):
    """A wopr widget, the content of which is rendered in XML as follows:

    <item col="5" row="9" colSpan="1" rowSpan="1">
        WIDGET_CONTENT
    </item>

    In theory, the available widgets are the ones that exist in the blessed and
    blessed-contrib projects; not all have been implemented here:
        [x] Line Chart
        [x] Markdown
        [x] Bar Chart
        [ ] Table
        [x] Donut
        [?] Stacked Bar Chart
        [ ] Map
        [ ] Gauge
        [ ] Stacked Gauge
        [ ] LCD Display
        [ ] Picture
        [ ] Sparkline
        [ ] Tree

    Not applicable because animated:
        [ ] Rolling Log
    """
    def __init__(self, col=0, row=0, colSpan=0, rowSpan=0, data=None, label=None):
        self.data = data or []
        self.col = col
        self.row = row
        self.colSpan = colSpan
        self.rowSpan = rowSpan
        self.label = label

    def make_markdown(self):
        return self.markdown.content()
        

    @property
    def content(self):
        ret = []
        ret.append('    <item col="{col}" row="{row}" colSpan="{colSpan}" rowSpan="{rowSpan}" label="{label}" >'.format(
            col=self.col,
            row=self.row,
            colSpan=self.colSpan,
            rowSpan=self.rowSpan,
            label=self.label,
            ))
        if self.data:
            ret.append(self.data)
        #ret.append(self.make_markdown())
        ret.append("    </item>\n")
        return "\n".join(ret).encode()


class Line:
    def __init__(self, title=None, style_line="red", x=[], y=[]):
        self.title = title
        self.style_line = style_line
        self.x = x
        self.y = y

    def get_x(self):
        return ",".join(self.x)
    def get_y(self):
        return ",".join(self.y)

    @property
    def content(self):
        ret = '<m title="{title}" style-line="{style_line}" x="{x}" y="{y}" />'.format(
            title = self.title,
            style_line = self.style_line,
            x = self.x,
            y = self.y,
            )
        return ret


class DonutChart(Widget):
    """A widget consisting of a collection of donuts."""
    def __init__(self,
                 arcWidth = 3,
                 border_type="line",
                 border_fg="gray",
                 data=None,
                 fill="white",
                 label=None,
                 radius=20,
                 remainColor="cyan",
                 spacing=1,
                 stroke="magenta",
                 yPadding=5,
                 col=None, row=None, colSpan=None, rowSpan=None):

        Widget.__init__(self, col, row, colSpan, rowSpan, label=label)
        self.arcWidth = arcWidth
        self.border_type = border_type
        self.border_fg = border_fg
        self.data = data
        self.radius = radius
        self.remainColor = remainColor
        self.spacing = spacing
        self.yPadding = yPadding

    @property
    def content(self):
        ret = []

        ret.append('    <item col="{col}" row="{row}" colSpan="{colSpan}" rowSpan="{rowSpan}" label="{label}" >'.format(
                    col=self.col,
                    row=self.row,
                    colSpan=self.colSpan,
                    rowSpan=self.rowSpan,
                    label=self.label,
                    ))

        # These are the attributes of the whole donut block
        donut = ['<donut ']
        donut.append('arcWidth="{}"'.format(self.arcWidth))
        donut.append('border-type="{}"'.format(self.border_type))
        donut.append('border-fg="{}"'.format(self.border_fg))
        donut.append('label="{}"'.format(self.label))
        donut.append('radius="{}"'.format(self.radius))
        donut.append('yPadding="{}"'.format(self.yPadding))
        donut.append('remainColor="{}"'.format(self.remainColor))   # doesn't work?
        donut.append('spacing="{}"'.format(self.spacing))
        donut.append('>')
        ret.append(" ".join(donut))

        # These are the attributes of the individual donuts
        ret.append("<data>")
        for donut in self.data:
            line = ['<m']
            line.append('label="{}"'.format(donut))
            line.append('percent="{}"'.format(self.data[donut][0]))
            line.append('color="{}"'.format(self.data[donut][1]))
            #line.append('remainColor="{}"'.format("cyan"))
            #line.append('stroke="{}"'.format("cyan"))
            #line.append('fill="{}"'.format("cyan"))
            #line.append('radius="{}"'.format("cyan"))
            #line.append('spacing="{}"'.format("cyan"))
            line.append('/> ')
            line = " ".join(line)
            ret.append(line)

        ret.append("</data>")
        ret.append("</donut>")
        ret.append("</item>")
        return "\n".join(ret)


class BarChart(Widget):
    """A bar chart."""
    def __init__(self,
                 barWidth=9,
                 barSpacing=1,
                 xOffset=10,
                 maxHeight=9, height="100%",
                 border_type="line", border_fg="gray",
                 data=None,
                 label=None,
                 col=None, row=None, colSpan=None, rowSpan=None):

        Widget.__init__(self, col, row, colSpan, rowSpan, label=label)

        self.barWidth = barWidth
        self.barSpacing = barSpacing
        self.xOffset = xOffset
        self.maxHeight = maxHeight
        self.height = height
        self.border_type = border_type
        self.border_fg = border_fg
        self.data = data

    @property
    def content(self):
        ret = []
        ret.append('<item col="{col}" row="{row}" colSpan="{colSpan}" rowSpan="{rowSpan}">'.format(
                    col=self.col,
                    row=self.row,
                    colSpan=self.colSpan,
                    rowSpan=self.rowSpan,
                    ))


        ret.append("".join([
            '<bar barWidth="{}" '.format(self.barWidth),
            'label="{}" '.format(self.label),
            'barSpacing="{}" '.format(self.barSpacing),
            'xOffset="{}" '.format(self.xOffset),
            'maxHeight="{}" '.format(self.maxHeight),
            'height="{}"  '.format(self.height),
            'border-type="{}" '.format(self.border_type),
            'border-fg="{}" '.format(self.border_fg),
            'data-titles="{}" '.format(",".join(self.data.keys())),
            'data-data="{}" />'.format(",".join([str(x) for x in self.data.values()])),
            ]))

        ret.append("\n\n")
        ret.append("    </item>")
        return "\n".join(ret)

class LineChart(Widget):
    """A line chart widget."""

    def __init__(self, xPadding=5, showLegend="true", legend_width=12, border_type="line", border_fg="gray", label=None,
                 col=None, row=None, colSpan=None, rowSpan=None):

        Widget.__init__(self, col, row, colSpan, rowSpan, label=label)
        self.xPadding = xPadding
        self.showLegend = showLegend
        self.legend_width = legend_width
        self.border_type = border_type
        self.border_fg = border_fg
        self.lines = []

    def add_row(self, *args):
        new_row = Row(*args)
        self.rows.append(new_row)
        self.rowSpan = max(self.rowSpan, len(self.rows))
        self.colSpan = max(self.colSpan, len(self.y))

    def add_line(self, *args, **kwargs):
        new_line = Line(*args, **kwargs)
        self.lines.append(new_line)

    @property
    def content(self):
        ret = []
        ret.append('    <item col="{col}" row="{row}" colSpan="{colSpan}" rowSpan="{rowSpan}">'.format(
                    col=self.col,
                    row=self.row,
                    colSpan=self.colSpan,
                    rowSpan=self.rowSpan,
                    ))

        ret.append('        <line xPadding="{xPadding}" showLegend="{showLegend}" legend-width="{legend_width}" border-type="{border_type}" border-fg="{border_fg}">'.format(
            xPadding=self.xPadding,
            showLegend=self.showLegend,
            legend_width=self.legend_width,
            border_type=self.border_type,
            border_fg=self.border_fg,
            ))
        ret.append("            <data>")
        # Add lines
        for line in self.lines:
            ret.append("                " + line.content)
        ret.append("            </data>")
        ret.append("        </line>")
        ret.append("    </item>")
        return "\n".join(ret)


class Markdown(Widget):
    """A Markdown object."""
    def __init__(self, data=None, style_paragraph="chalk.white",
                 style_strong = "chalk.cyan.underline",
                 style_em = "chalk.green",
                 border_type = "line",
                 border_fg = "gray",
                 label = None,
                 col=None, row=None, colSpan=None, rowSpan=None):

        Widget.__init__(self, col, row, colSpan, rowSpan, label=label)

        # markdown styles
        self.style_paragraph = style_paragraph
        self.style_strong = style_strong
        self.style_em = style_em
        self.border_type = border_type
        self.border_fg = border_fg
        self.data = self.escape(data)
        self.label = label

    def escape(self, data):
        if '&' in data:
            data = data.replace('&', '&amp;')
        if '<' in data:
            data = data.replace('<', '&amp;')
        if '>' in data:
            data = data.replace('>', '&amp;')
        return data

    def stylize(self, line):
        """Apply some colors to Markdown text."""
        if line.startswith('##'):
            line = click.style(line, bold=True)
        if line.startswith('# '):
            line = click.style(line, bold=True)

        if line.count('**') == 2:
            line = line.split('**')
            line = line[0] + click.style(line[1], bold=True) + line[2]
        if line.count('_') == 2:
            line = line.split('_')
            line = line[0] + click.style(line[1], underline=True) + line[2]
        return line

    @property
    def content(self):
        if isinstance(self.data, list):
            self.data = [self.stylize(line) for line in self.data]
            self.data = "\n".join(self.data)
        if self.data:
            self.data = self.data.replace('\n', u' &#10; ')

        ret = []
        ret.append('<item col="{col}" row="{row}" colSpan="{colSpan}" rowSpan="{rowSpan}">'.format(
                    col=self.col,
                    row=self.row,
                    colSpan=self.colSpan,
                    rowSpan=self.rowSpan,
                    ))

        ret.append("".join([
            '       <markdown style-paragraph="{style_paragraph}" '.format(style_paragraph = self.style_paragraph),
            'style-strong="{style_strong}" '.format(style_strong = self.style_strong),
            'style-em="{style_em}" '.format(style_em = self.style_em),
            'border-type="{border_type}" '.format(border_type = self.border_type),
            'label="{label}" '.format(label = self.label),
            'border-fg="{border_fg}"> '.format(border_fg = self.border_fg),
        ]))

        ret.append("\n")
        ret.append("\t<markdown>\n")
        ret.append("\t\t" + self.data)
        ret.append("\n")
        ret.append("        </markdown>\n")
        ret.append("</markdown>\n")
        ret.append("    </item>")
        return "\n".join(ret)


class Row:
    """A row in a table object."""
    def __init__(self, items):
        self.items = items

    @property
    def content(self):
        return ",".join([str(x) for x in self.items])

class Gauge(Widget):
    """A progress gauge."""
       #var gauge = contrib.gauge({label: 'Progress', stroke: 'green', fill: 'white'})
       #gauge.setPercent(25)
    def __init__(self, label = None,
                 stroke = "green", fill = "white", percent = 50,
                 border={"type": "line", "fg": "cyan"},
                 border_type="line", border_fg="gray",
                 col=None, row=None, colSpan=None, rowSpan=None):

        Widget.__init__(self, col, row, colSpan, rowSpan, label=label)
        self.stroke = stroke
        self.fill = fill
        self.percent = percent
        self.border = border
        self.border_type = border_type
        self.border_fg = border_fg

    @property
    def content(self):
        ret = []
        ret.append('<item col="{col}" row="{row}" colSpan="{colSpan}" rowSpan="{rowSpan}" >'.format(
                    col=self.col,
                    row=self.row,
                    colSpan=self.colSpan,
                    rowSpan=self.rowSpan,
                    ))
        ret.append("".join([
            '<gauge percent="{}" ',
            'label="{}" ',
            'stroke="{}" ',
            #'border="{}" ',
            'border-type="{}" ',
            'border-fg="{}" ',
            '>',
            ]).format(
                self.percent,
                self.label,
                self.stroke,
                #self.border,
                self.border_type,
                self.border_fg,
                ))

        ret.append("foo")
        ret.append("</gauge>")
        ret.append("</item>")
        return "\n".join(ret)


class Table(Widget):
    """A table object."""

    def __init__(self, fg="white",
                 width="30%", height="30%",
                 border={"type": "line", "fg": "cyan"},
                 border_type="line", border_fg="gray",
                 columnSpacing=8,
                 columnWidth=None,
                 interactive="false",
                 label = None,
                 selectedFg = None,
                 selectedBg = None,
                 keys = False,
                 data = {},
                 col=None, row=None, colSpan=None, rowSpan=None):

        Widget.__init__(self, col, row, colSpan, rowSpan, label=label)
        self.fg = fg
        self.keys = keys
        self.width = width
        self.height = height
        self.border = border
        self.border_type = border_type
        self.border_fg = border_fg
        self.columnSpacing = columnSpacing
        self.interactive = interactive
        self.selectedFg = selectedFg
        self.selectedBg = selectedBg
        self.data = data
        self.rows = data["rows"]
        self.headers = data["headers"]

    @property
    def data_headers(self):
        """Return the table headers."""
        headers = self.data["headers"]
        return ",".join(headers)

    def fill_rows(self):
        """Fill rows with empty strings to avoid annoying "RangeError: Invalid array length" error."""
        # FIXME: this doesn't work...
        maxlen = max([len(row) for row in self.rows])
        maxlen = max(maxlen, len(self.headers))
        for row in self.rows:
            while len(row) < maxlen:
                row.append(" ")
            #print(row, file=sys.stderr)
        while len(self.headers) < maxlen:
            self.headers.append(" ")
        #print(self.data_headers, file=sys.stderr)
        #print(self.headers, file=sys.stderr)
        #print(maxlen, file=sys.stderr)
        assert len(self.headers) == maxlen

    @property
    def columnWidth(self):
        """Return the width of each column."""
        widths = [len(header) for header in self.headers]
        for row in self.rows:
            row_widths = [len(str(x)) for x in row]
            widths = [max(x, y) for (x, y) in zip (widths, row_widths)]
        return ",".join([str(x) for x in widths])

    @property
    def content(self):
        ret = []
        ret.append('<item col="{col}" row="{row}" colSpan="{colSpan}" rowSpan="{rowSpan}" >'.format(
                    col=self.col,
                    row=self.row,
                    colSpan=self.colSpan,
                    rowSpan=self.rowSpan,
                    ))

        ret.append((
                '           <table '
                'border-type="{border_type}" border-fg="{border_fg}" '
                'columnSpacing="{columnSpacing}" columnWidth="{columnWidth}" '
                'data-headers="{data_headers}" '
                'fg="{fg}" '
                'height="{height}" '
                'interactive="{interactive}" '
                'keys="{keys}" '
                'label="{label}" '
                'width="{width}" '
                'selectedBg="{selectedBg}" '
                'selectedFg="{selectedFg}" '
                '> '
                    .format(
                            border_type=self.border_type,
                            border_fg=self.border_fg,
                            columnSpacing=self.columnSpacing,
                            columnWidth=self.columnWidth,
                            data_headers=self.data_headers,
                            fg=self.fg,
                            height=self.height,
                            interactive=self.interactive,
                            keys=self.keys,
                            label=self.label,
                            selectedBg=self.selectedBg,
                            selectedFg=self.selectedFg,
                            width=self.width,
                        )))

        ret.append("            <data-data>")
        self.fill_rows()
        assert len(self.headers) == len(self.rows[0])
        for row in self.rows:
            ret.append("            " + ",".join([str(x) for x in row]))
        ret.append("            </data-data>")
        ret.append("         </table>")
        ret.append("     </item>")

        return "\n".join(ret)

class Spedometer(Widget):
    """
    This is a made-up class but I like it.
    """
    fancy_grid = [
        "╒", "═", "╤", "═", "╕",
        "│", " ", "╪", " ", "│",
        "╞", " ", "╪", " ", "╡",
        "╘", "═", "╧", "═", "╛"
        ]

    toc = [
        "╒══════════════ Welcome to the professional resume of A.J. Bowen ══════════════════════╕",
        "│                                                                                          │",
        "│  1. This screen                                                                          │",
        "│  2. Skills                                                                               │",
        "│  3. Experience                                                                           │",
        "│  4. Languages                                                                            │",
        "│                                                                                          │",
        "│  To view all slides (press enter to move to next slide; press Ctrl+C to exit)            │",
        "│                                                                                          │",
        "│    $ p=0; while true; do curl localhost/$((p++))\?cols=$((COLUMNS)); read; done          │",
        "│                                                                                          │",
        "│  To view a specific slide:                                                               │",
        "│                                                                                          │",
        "│    $ curl -N cv.soulshake/3                                                              │",
        "│                                                                                          │",
        "│  Options (URL paramters):                                                                │",
        "│                                                                                          │",
        "│   \?auto                 Advance through slides automatically (5 seconds each)           │",
        "│   \&cols=$((COLUMNS))    Specify number of rows                                          │",
        "│   \&rows=$((LINES))      Specify number of columns                                       │",
        "│   \&terminal=xterm       Specify your terminal                                           │",
        "│                                                                                          │",
        "│  You can infer them automatically from your environment:                                 │",
        "│                                                                                          │",
        "│    $ curl -N cv.soulshake.net\?\&cols=$((COLUMNS))\&rows=$((LINES-5))\&terminal=${TERM}  │",
        "│                                                                                          │",
        "│                                                                                          │",
        "╘══════════════════════════════════════════════════════════════════════════════════════════╛"]

    @property
    def content(self):
        ret = [
        "  .",
"                   90    100                          90    100 ",
"              80  \           110                80              110",
"                   \ ",
"          70        \             120        70                      120",
"                     \ ",
"        60            \             130    60                          130",
"                       O                                  O",
"        50                          140    50              \           140",
"                                                            \ ",
"         40                        150      40               \        150",
"                      mph                                mph  \ ",
"            30                  160            30              \   160",
"          This is your CV on LinkedIn     This is your CV on the command line"]

        return "\n".join(ret)

