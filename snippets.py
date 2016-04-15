#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
"""
This library is intended to generate XML suitable for being served by a wopr server.
"""


class Circle:
    """A circle."""
    def __init__(self, radius):
        self.radius = radius

    def content(self):
        ret = [
                "           %%%    %%%",
                "      %%%              %%%",
                "",
                "  %%%                      %%%",
                "",
                " %%%                         %%%",
                "",
                " %%%                         %%%",
                "",
                " %%%                        %%%",
                "",
                "    %%%                  %%%",
                "",
                "          %%%     %%%",
                ]
        return "\n".join(ret)

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
        [ ] Donut
        [ ] Stacked Bar Chart
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
    def __init__(self, col=0, row=0, colSpan=0, rowSpan=0, markdown=None):
        #colSpan = max([len(x) for x in ret])/16
        #rowSpan = len(ret)/5
        self.data = []
        self.col = col
        self.row = row
        #self.colSpan = colSpan
        #self.rowSpan = rowSpan

        if markdown:
            self.markdown = Markdown(markdown)

    def make_markdown(self):
        return self.markdown.content()
        

    @property
    def content(self):
        ret = []
        ret.append('    <item col="{col}" row="{row}" colSpan="{colSpan}" rowSpan="{rowSpan}">'.format(
            col=self.col,
            row=self.row,
            colSpan=self.colSpan,
            rowSpan=self.rowSpan,
            ))
        ret.append(self.make_markdown())
        ret.append("    </item>\n")
        return "\n".join(ret).encode()


class Line(list):
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


class LineChart(Widget):
    """A line chart widget."""

    def __init__(self, xPadding=5, showLegend="true", legend_width=12, border_type="line", border_fg="gray",
                 col=None, row=None, colSpan=None, rowSpan=None):
        Widget.__init__(self, col, row, colSpan, rowSpan)
        self.xPadding = xPadding
        self.showLegend = showLegend
        self.legend_width = legend_width
        self.border_type = border_type
        self.border_fg = border_fg
        self.lines = []

    @property
    def colSpan(self):
        # FIXME: this is nonsense
        #colSpan = cols/16
        #rowSpan = rows/4
        return max([len(x) for x in self.lines])/4

    @property
    def rowSpan(self):
        return len(self.lines)/4

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


class BarChart(Widget):
    """A bar chart."""
    def __init__(self,
                 barWidth=1,
                 barSpacing=1,
                 xOffset=10,
                 maxHeight=5, height="100%",
                 border_type="line", border_fg="gray",
                 data_titles=[], data_data=[],
                 col=None, row=None, colSpan=None, rowSpan=None):

        Widget.__init__(self, col, row, colSpan, rowSpan)
        self.barWidth = barWidth
        self.barSpacing = barSpacing
        self.xOffset = xOffset
        self.maxHeight = maxHeight
        self.height = height
        self.border_type = border_type
        self.border_fg = border_fg
        self.data_titles = data_titles
        self.data_data = data_data
        self.bars = []

    @property
    def colSpan(self):
        # FIXME
        return 8 #len(self.rows)/4

    @property
    def rowSpan(self):
        # FIXME
        return 8 #max([len(x) for x in self.rows])/4

    def add_bar(self, title, data):
        self.data_titles.append(title)
        self.data_data.append(data)
        # or...
        self.bars.append((title, data))

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
            'barSpacing="{}" '.format(self.barSpacing),
            'xOffset="{}" '.format(self.xOffset),
            'maxHeight="{}" '.format(self.maxHeight),
            'height="{}"  '.format(self.height),
            'border-type="{}" '.format(self.border_type),
            'border-fg="{}" '.format(self.border_fg),
            'data-titles="{}" '.format(",".join([x[0] for x in self.bars])), #self.titles)),
            'data-data="{}" />'.format(",".join([str(x) for x in self.data_data])),
            ]))

        ret.append("\n")
        #ret.append("\t\t" + self.data_data)
        ret.append("\n")
        ret.append("    </item>")
        return "\n".join(ret)


class Markdown(Widget):
    """A Markdown object."""
    def __init__(self, data=None, style_paragraph="chalk.white",
                 style_strong = "chalk.cyan.underline",
                 style_em = "chalk.green",
                 border_type = "line",
                 border_fg = "gray",
                 col=None, row=None, colSpan=None, rowSpan=None):

        Widget.__init__(self, col, row, colSpan, rowSpan)

        # markdown styles
        self.style_paragraph = style_paragraph
        self.style_strong = style_strong
        self.style_em = style_em
        self.border_type = border_type
        self.border_fg = border_fg
        self.data = self.escape(data)
        self.raw_list = data.split('\n') if not isinstance(data, list) else data

    @property
    def colSpan(self):
        #return len(self.raw_list)/4
        return 8

    @property
    def rowSpan(self):
        #return max([len(x) for x in self.raw_list])/8
        return 8

    def escape(self, data):
        if '&' in data:
            data = data.replace('&', '&amp;')
        if '<' in data:
            data = data.replace('<', '&amp;')
        if '>' in data:
            data = data.replace('>', '&amp;')
        if '\n' in data:
            data = data.replace('\n', ' &#10; ')
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
            self.raw_list = self.data
            self.data = [self.stylize(line) for line in self.data]
            self.data = "\n".join(self.data)
        else:
            self.raw_list = self.data.split('\n')

        self.data = self.escape(self.data)

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


class Row(list):
    """A row in a table object."""
    def __init__(self, items):
        self.items = items

    @property
    def content(self):
        return ",".join([str(x) for x in self.items])

class Table(Widget):
    """A table object."""

    def __init__(self, fg="white",
                 width="30%", height="30%",
                 border_type="line", border_fg="gray",
                 columnSpacing=8,
                 interactive="false",
                 col=None, row=None, colSpan=None, rowSpan=None):
        Widget.__init__(self, col, row, colSpan, rowSpan)
        self.fg = fg
        self.width = width
        self.height = height
        self.border_type = border_type
        self.border_fg = border_fg
        self.columnSpacing = columnSpacing
        self.interactive = interactive
        self.data = {}
        self.rows = []

    def add_row(self, *args):
        self.rows.append(Row(*args))
        #self.raw_list = self.rows

    def add_columns(self, headers):
        self.headers = headers

    @property
    def colSpan(self):
        #return len(self.rows)/4
        return 8

    @property
    def rowSpan(self):
        #return max([len(x) for x in self.rows])/4
        return 8

    @property
    def data_headers(self):
        """Return the table headers."""
        return ",".join(self.headers)

    def fill_rows(self):
        """Fill rows with empty strings to avoid annoying "RangeError: Invalid array length" error."""
        maxlen = max([len(row.items) for row in self.rows])
        maxlen = max(maxlen, len(self.headers))
        for row in self.rows:
            while len(row.items) < maxlen:
                row.items.append("")
        while len(self.headers) < maxlen:
            self.headers.append("")
        assert len(self.headers) == maxlen

    @property
    def columnWidth(self):
        """Return the width of each column."""
        widths = [len(header) for header in self.headers]
        for row in self.rows:
            row_widths = [len(str(x)) for x in row.items]
            widths = [max(x, y) for (x, y) in zip (widths, row_widths)]
        return ",".join([str(x) for x in widths])

    @property
    def content(self):
        ret = []
        ret.append('<item col="{col}" row="{row}" colSpan="{colSpan}" rowSpan="{rowSpan}">'.format(
                    col=self.col,
                    row=self.row,
                    colSpan=self.colSpan,
                    rowSpan=self.rowSpan,
                    ))

        ret.append((
                '           <table fg="{fg}" width="{width}" height="{height}" '
                'border-type="{border_type}" border-fg="{border_fg}" '
                'columnSpacing="{columnSpacing}" columnWidth="{columnWidth}" '
                'data-headers="{data_headers}" interactive="{interactive}"> '
                    .format(
                            fg=self.fg,
                            width=self.width,
                            height=self.height,
                            border_type=self.border_type,
                            border_fg=self.border_fg,
                            columnSpacing=self.columnSpacing,
                            columnWidth=self.columnWidth,
                            data_headers=self.data_headers,
                            interactive=self.interactive,
                        )))

        ret.append("            <data-data>")
        self.fill_rows()
        assert len(self.headers) == len(self.rows[0].items)
        for row in self.rows:
            ret.append("            " + row.content)
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

