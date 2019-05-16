#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import OrderedDict
from widgets import *
import click

# For some reason the first line sometimes gets formatted weird
# This invisible placeholder seems to be a functional workaround
placeholder = click.style(u" ", fg="white")


def processes_table():
    table = {
        "border": {"type": "line", "fg": "cyan"},
        "columnSpacing": 6,
        "columnWidth": [16, 12, 12],
        "fg": "green",
        "height": "30%",
        "interactive": "true",
        "keys": "true",
        "label": "Active Processes",
        "selectedFg": "white",
        "selectedBg": "blue",
        "width": "10%",
    }

    data = {
        "headers": ["Autodidact Process", "Cpu (%)", "Memory", "Comment"],
        "rows": [
            ["German", 12, 13, "Host 'Berlin' unresponsive; trying again"],
            [
                "Docker",
                15,
                26,
                "Last command 'containerize-all-the-desktop-apps.sh' cannot stop itself",
            ],
            ["node.js", 5, 16, "Parent process 'frontend' is dirty"],
            ["Deployment automation", 12, 8.7, "Onscreen"],
            ["blog.soulshake.net", 3, 12.5, "Deployment in progress"],
            ["Ruby/Rails", 8, 6.2, "Recovering"],
            ["Job search", 0, 0, "Finished"],
        ],
    }

    ret = Table(col=0, row=0, colSpan=8, rowSpan=5, data=data, **table)
    return ret


def languages_donuts():
    data = OrderedDict({})
    data["Russian"] = [10, "red"]
    data["German"] = [28, "yellow"]
    data["English"] = [99, "green"]
    data["French"] = [89, "blue"]
    data["Spanish"] = [60, "magenta"]

    ret = DonutChart(
        col=0, row=0, colSpan=15, rowSpan=5, label="Human languages", data=data
    )
    return ret


def languages_table():
    data = {
        "headers": ["Language", "time", "DuoLingo level", "ease", "status"],
        "rows": [
            ["Russian", "1y", 16, "10%", "{red-fg} caveperson"],
            ["German", "2y", 187, "39%", "{yellow-fg} rather clumsy"],
            ["Italian", "6 mo", 16, "15%", "{yellow-fg} I manage"],
            ["English", ">10y", 999, "99%", "{green-fg} native speaker"],
            ["French", ">10y", 899, "89%", "{blue-fg} fluent"],
            ["Spanish", "n/a", 94, "40%", "{magenta-fg} passive"],
        ],
    }

    table = {"label": "Details"}

    languages = Table(col=2, row=2, colSpan=5, rowSpan=3, data=data, **table)
    return languages


def looking_for():
    label = "What am I looking for?"
    ret = (
        placeholder
        + """

I'm pretty happy where I'm at right now.

My ideal roles involve some combination of the following:

  - writing useful tools (libraries, CLIs) that improve efficiency,
  - playing with APIs, connecting services, making mashups and integrations,
  - automating all the things,
  - documenting all the things,
  - making the world better, one way or another

Right now some of the more abstract tools* I'm equipped with are:

  - an incorrigible curiosity,
  - a sort of fierce empathy,
  - an incorruptible rage at injustice,
  - a relentless stubborn determination when faced with a problem or a mystery,
  - an obsession with well-made things and awesome documentation,
  - an endless supply of ideas and hypotheses,
  - a tiny bit of a bunch of other things, due to the aforementioned curiosity,
  - an apparent intuition for seeing causal relationships in the "big picture"


\* several of these qualities have gotten me into trouble at some point, so YMMV.
    """
    )
    ret = Markdown(colSpan=6, rowSpan=8, data=ret, col=3, row=3, label=label)
    return ret


def contact():
    rows = []
    rows.append([click.style("Site", fg="red"), "soulshake.net"])
    rows.append([click.style("Email", fg="yellow"), "aj@soulshake.net"])
    rows.append([click.style("Github", fg="green"), "https://github.com/soulshake"])
    rows.append([click.style("Twitter", fg="blue"), "https://twitter.com/s0ulshake"])
    rows.append(
        [click.style("LinkedIn", fg="magenta"), "https://www.linkedin.com/in/ajbowen"]
    )

    rows = [[row[0].rjust(30), click.style(row[1], fg="cyan")] for row in rows]
    rows = ["  ".join(row) for row in rows]
    table = "\n".join(rows)

    contact = [
        placeholder,
        "Say hi:",
        table,
        "For more info, see:",
        click.style(
            "http://blog.soulshake.net/2016/04/command-line-resume/", fg="cyan"
        ),
        "                   Thanks!",
        "                   Love, AJ" "",
    ]
    contact = "\n\n".join(contact)
    label = "Is this thing on?"
    about = Markdown(colSpan=4, rowSpan=6, data=contact, col=3, row=3, label=label)
    return about


def overview():
    label = click.style("Overview", fg="white")
    about_me = [
        placeholder,
        "Name".ljust(20) + click.style("AJ Bowen", fg="green", bold=True),
        "Location".ljust(20) + click.style("Berlin and Kansas City", fg="green"),
        "Employment State".ljust(20)
        + click.style("ACTIVE", dim=True, fg="green", reverse=True),
        "Employment Status".ljust(20)
        + click.style("Search in progress...", dim=True, fg="yellow"),
        "Mobility".ljust(20) + click.style("Flexible", fg="green"),
        "Nerdery Level".ljust(20) + click.style("CRITICAL", fg="red", reverse=True),
    ]

    about_me = "\n".join(about_me)
    about = Markdown(colSpan=4, rowSpan=4, data=about_me, col=3, row=3, label=label)
    return about


def scorebar(level, total=15, char=u"■ "):
    fg = "green"
    if level <= total * 0.667:
        fg = "yellow"
    if level <= total * 0.334:
        fg = "red"

    fill_char = click.style(char, fg=fg)
    empty_char = click.style(char, fg="white")
    filled = fill_char * level
    empty = empty_char * (total - level)

    return filled + empty


def weapons():
    width = 17
    d = OrderedDict({})
    d["Python"] = 14
    d["XML-RPC"] = 14
    d["REST"] = 12
    d["Linux"] = 13
    d["Bash"] = 12
    d["Git"] = 12
    d["SQL"] = 10
    d["GoLang"] = 13
    d["Ruby/Rails"] = 8
    d["C"] = 5
    d["C++"] = 3

    ret = [placeholder]
    for key in d:
        ret.append(key.ljust(width) + scorebar(d[key]))

    return Markdown(
        colSpan=4, rowSpan=4, data="\n".join(ret), col=0, row=6, label="Weapons"
    )


def attributes():
    """Some of my characteristics."""
    # Skipping: optimism, integrity
    width = 17

    attributes = OrderedDict({})
    attributes["Race"] = click.style("Hybrid Software Engineer", bold=True)
    attributes["Alignment"] = "Chaotic Good"
    attributes["Empathy"] = 13
    attributes["Willpower"] = 12
    attributes["Creativity"] = 12
    attributes["Typing speed"] = 13
    attributes["Idealism"] = 12
    attributes["Curiosity"] = 11
    attributes["Punctuality"] = 6
    attributes["Willingness to \n  relocate to  "] = ""
    attributes["  San Francisco"] = 3

    ret = [placeholder]
    for key in attributes:
        if isinstance(attributes[key], int):
            ret.append(key.ljust(width) + scorebar(attributes[key]))
        else:
            ret.append(key.ljust(width) + click.style(attributes[key], fg="green"))

    ret = "\n".join(ret)
    attributes = Markdown(
        colSpan=4, rowSpan=4, data=ret, col=3, row=3, label="Attributes"
    )

    return attributes


def other_experience():
    label = "Unprofessional Experience"
    blurb = [
        placeholder,
        "I've danced myself into a trance in Berlin nightclubs and Haitian RaRas. I've ",
        "seen the inside of several jail cells. I tried to burn a bra once but it wouldn't catch.\n",
        "I've organized underground newspapers, backyard boxing leagues and protests, ",
        "as well as several successful dinner parties.\n",
        "If working for your company will help me expand this section, please reach out ASAP.",
    ]
    other_exp = Markdown(
        colSpan=6, rowSpan=3, data="\n".join(blurb), col=3, row=3, label=label
    )
    return other_exp


def professional_experience():
    label = "Professional Experience"

    blurb = [placeholder]

    positions = [
        [
            "Infrastructure Engineer",
            "Travis CI",
            "July 2017",
            "Present",
            "Berlin/Remote",
        ],
        ["Solutions Engineer", "Convox", "October 2016", "April 2017", "Remote"],
        [
            "DevOps Engineer",
            "Voteraide (volunteer)",
            "May 2016",
            "September 2016",
            "Remote",
        ],
        [
            "Chief of Counter-bullshit operations",
            "Gandi.net",
            "October 2013",
            "December 2015",
            "San Francisco",
        ],
        [
            "Level 1+ Support Representative",
            "Gandi.net",
            "February 2012",
            "October 2013",
            "Remote/Lawrence, KS)",
        ],
        [
            "Federal Student Aid question answerer",
            "Vangent, Inc",
            "2010",
            "2011",
            "Lawrence, KS",
        ],
    ]

    for position in positions:
        position[0] = position[0].rjust(20)
        blurb.append(
            "{} @{}: {} - {} ({})".format(
                click.style(position[0], fg="magenta", bold=True).rjust(50),
                click.style(position[1], fg="yellow").rjust(13),
                position[2],
                position[3],
                position[4],
            )
        )

    blurb.append("\n")
    blurb.append(
        click.style("Previous positions", fg="blue") + ": See LinkedIn profile"
    )
    blurb.append(
        click.style("Details on recent positions", fg="blue") + ": See next slide"
    )
    blurb = Markdown(colSpan=6, rowSpan=3, data=blurb, col=0, row=0, label=label)
    return blurb


def awards():
    ret = [
        placeholder,
        "Global Awareness Certification: 2010",
        "Harley S Nelson scholar: 2009",
        "Undergraduate Research Award: 2009",
        "Award for excellence in FREN 450: 2009",
        "KU Honor Roll: 2007, 2008, 2009",
        "Teaching grant (Haiti): Spring 2008",
        "Topeka Credit Union Scholarship: 2004",
        "Mater Dei scholarship: 2004, 2005, 2006",
        "Most improved in beginner motorcycle class: 2005",
        "Hardest worker, SHHS Track team: 2000",
    ]
    ret = Markdown(colSpan=4, rowSpan=4, data=ret, col=0, row=0, label="Awards")
    return ret


def intro():
    intro = [
        click.style(".", dim=True),
        "Hi, I'm {}.".format(click.style("AJ", fg="red")),
        "I'm a {} with a strong interest in ".format(
            click.style("Python developer", fg="yellow")
        ),
        "APIs, CLIs and subverting the dominant paradigm.",
        "This is my resume.",
        "",
        "Note: this is primarily intended for command-line addicts.",
        "A more conventional version can be found on LinkedIn.",
    ]
    intro = [click.unstyle(item).center(80) for item in intro]
    intro = "\n".join(intro)
    intro = intro.replace("APIs", click.style("APIs", fg="green"))
    intro = intro.replace("CLIs", click.style("CLIs", fg="blue"))
    intro = intro.replace(
        "subverting the dominant paradigm",
        click.style("subverting the dominant paradigm", fg="magenta"),
    )

    colSpan = 5
    rowSpan = 3.5

    ret = Markdown(data=intro, colSpan=colSpan, rowSpan=rowSpan, label="")
    return ret


def toc():
    """
    u"   {}".format(click.style("p=1; while true; do curl cv.soulshake.net/$((p++))\?cols=$((COLUMNS)); read; done", fg='green', bold=True)),
    u"",
    u" (press enter to move to next slide; press Ctrl+C to exit)",
    u"",
    u"  Contents:",
    u"    0. This screen",
    u"    1. Overview",
    u"    2. Active processes",
    u"    3. Skills",
    u"    4. Languages",
    u"    5. Experience",
    u"    6. Experience (details)",
    u"    7. About",
    """

    ret = [
        placeholder,
        u"",
        u" To view all slides, run:",
        u"   {}".format(
            click.style(
                "p=1; while [ $p -lt 9 ]; do curl -N cv.soulshake.net/$((p++)); read; done",
                fg="green",
                bold=True,
            )
        ),
        u"",
        u"  To view a specific slide:",
        u"    {}".format(
            click.style("curl -N cv.soulshake.net/3/\?cols=$((COLUMNS))", fg="green")
        ),
    ]

    colSpan = 5
    rowSpan = 9

    ret = "\n".join(ret)
    ret = Markdown(
        data=ret,
        colSpan=colSpan,
        rowSpan=rowSpan,
        label="The very professional resume of A.J. Bowen",
    )
    return ret


def exp_travis():
    label = "[Experience] Travis CI"
    width = 15
    d = OrderedDict({})
    d["Employer"] = "Travis CI"
    d["Location"] = "Berlin, Germany (remote)"
    d["Dates"] = "July 2017 to May 2019"
    d["2017-2019"] = "Build infrastructure engineer"
    d["A.K.A."] = [
        "DevOps",
        "EC2 specialist",
        "Docker specialist",
        "Automation specialist",
        "Chaos monkey",
    ]
    d["A.K.A."] = [click.style(x, fg="yellow") for x in d["A.K.A."]]
    ret = [placeholder]
    for key in d:
        styles = {"fg": "green"}

        if key in ["2017-2019"]:
            styles["fg"] = "yellow"
            styles["reverse"] = True
            styles["bold"] = True

        if isinstance(d[key], list):
            d[key] = "\n".join(["{}{}".format(" ".ljust(20), x) for x in d[key]])
            d[key] = d[key][20:]

        ret.append(key.ljust(width) + click.style(d[key], **styles))

    ret = "\n".join(ret)
    ret = Markdown(colSpan=3, rowSpan=7, data=ret, col=3, row=3, label=label)

    return ret


def exp_gandi():
    label = "[Experience] Gandi.net"
    width = 15

    d = OrderedDict({})
    d["Employer"] = "Gandi.net \o/"
    d["Location"] = "San Francisco, CA"
    d["Dates"] = "February 2012 to December 2015"
    d["2013-2015"] = "Counter-bullshit operations"
    d["A.K.A."] = [
        "Developer advocate",
        "API evangelist",
        "Technical community manager",
        "Chaos monkey",
        "Emergency PR strategist",
        "Open source champion",
        "Automation specialist",
        "Special projects",
        "QA intern",
        "Workshop administrator",
        "Swag dealer",
    ]
    d["A.K.A."] = [click.style(x, fg="yellow") for x in d["A.K.A."]]

    d["2012-2013"] = "Level 1+ Support Agent"
    d["A.K.A. "] = [
        "Support ticket answerer person",
        "Documentation tweaker",
        "Bug hunter",
        "Twitter person",
        "Question asker",
    ]
    d["A.K.A. "] = [click.style(x, fg="yellow") for x in d["A.K.A. "]]

    ret = [placeholder]
    for key in d:
        styles = {"fg": "green"}

        if key in ["2013-2015", "2012-2013"]:
            styles["fg"] = "yellow"
            styles["reverse"] = True
            styles["bold"] = True

        if isinstance(d[key], list):
            d[key] = "\n".join(["{}{}".format(" ".ljust(20), x) for x in d[key]])
            d[key] = d[key][20:]

        ret.append(key.ljust(width) + click.style(d[key], **styles))

    ret = "\n".join(ret)
    ret = Markdown(colSpan=3, rowSpan=7, data=ret, col=3, row=3, label=label)

    return ret


def exp_travis_tldr():
    blurb = """
Travis CI has been an incredible place to work. I will be forever grateful for the experience of working with one of the most
amazing groups of humans ever.
    """

    label = "TL;DR"
    ret = [placeholder]
    ret.append(blurb)

    ret = "\n".join(ret)
    ret = Markdown(colSpan=7.5, rowSpan=4, data=ret, col=3, row=3, label=label)

    return ret


def exp_travis_details():
    label = "Details"
    blurb = """
Soon after joining Travis, I set out to become an expert on our EC2 / Docker-based infrastructure. As part of this effort, I:\n\n
- noticed that our CPUs-per-job allocation didn't match what we we advertised in documentation and identified and fixed the relevant bug\n
- containerized numerous microservices\n
- made numerous improvements to EC2 scaling behavior in an effort to reduce spurious pager alerts\n
- built tools to detect and remove stalled EC2 instances, resulting in cost savings\n
- helped build tooling to benchmark instance performance as part of an effort to review overall EC2 costs\n\n
I also helped drive efforts to identify and mitigate bitcoin mining and related abuse patterns, authoring a number of tools to help others identify and deal with these problems.\n\n
I shared on-call responsibilities and was involved in resolving a number of difficult production incidents, as well as tracking down some most disruptive and evasive bugs.
"""

    ret = [placeholder]
    ret = []
    ret.append(blurb)
    from IPython import embed

    # embed()

    ret = "\n".join(ret)
    ret = Markdown(colSpan=4.5, rowSpan=7, data=ret, col=3, row=3, label=label)

    return ret


def exp_gandi_tldr():
    blurb = """My initial role at Gandi was entry-level support: troubleshooting and explaining issues relating to domain
names, DNS, SSL certs and basic hosting.\n\n
My curiosity and interest in this role led me to specialize in more technical hosting issues, while helping to hire,
train and mentor new employees, edit blog posts, and generally pitch in anywhere I could be helpful.\n\n
This versatility led me to be promoted to a so-called Community Manager role in our new San Francisco office.\n\n
From the time I was hired (near the beginning of Gandi's expansion into the U.S.) to the time I left, I had played a
role in nearly every aspect of our growth in the United States.
    """

    label = "TL;DR"
    ret = [placeholder]
    ret.append(blurb)

    ret = "\n".join(ret)
    ret = Markdown(colSpan=7.5, rowSpan=4, data=ret, col=3, row=3, label=label)

    return ret


def exp_gandi_details():
    label = "Details"

    blurb = """
I interacted with various tech communities, online and at industry events,
connecting with developers and helping them make the most of Gandi's domain,
SSL and hosting APIs.

I was the primary technical contact for Gandi resellers in the U.S.,
escalating to the CTO where appropriate.

Internally, I worked with engineers, product managers and support to improve
Gandi's APIs, web interface, documentation and open source presence based
on feedback collected from the community.

I shaped much of Gandi's voice via blog posts, newsletters and social media
interactions. I created, edited and localized a wide variety of technical
documentation, emergency communications and product communications.

I guided and managed Gandi's supported initiatives and open source projects,
organizing various campaigns and partnerships for our mutual benefit.

I tested and documented a huge number of Gandi's products and features.

Mostly: I was ready for anything, which usually happened at least twice a
week.\n\n
"""

    ret = [placeholder]
    ret.append(blurb)

    ret = "\n".join(ret)
    ret = Markdown(colSpan=4.5, rowSpan=7, data=ret, col=3, row=3, label=label)

    return ret


def skills_bar_chart():
    data = OrderedDict()
    data["Python"] = 9.5
    data["Bash"] = 8.5
    data["AWS"] = 7.5
    data["DNS"] = 9
    data["Docker"] = 9
    data["Linux"] = 8
    data["Automation"] = 8
    colSpan = 6
    rowSpan = 4
    barchart = BarChart(
        col=1,
        row=1,
        colSpan=colSpan,
        rowSpan=rowSpan,
        label="Computery Skills",
        data=data,
    )
    return barchart


def skills_other_bar_chart():
    data = OrderedDict()
    data["People"] = 8
    data["Learning"] = 7
    data["Singing"] = 1
    data["Chaos"] = 6
    data["Coloring"] = 5
    data["Genealogy"] = 9
    data["Lockpicking"] = 4

    colSpan = 6
    rowSpan = 4

    ret = BarChart(
        col=1, row=1, colSpan=colSpan, rowSpan=rowSpan, label="Other Skills", data=data
    )
    return ret


def employment_progress():
    # Note to self: Keep track of this and increment for each hit?
    colSpan = 6
    rowSpan = 2
    data = {"percent": 89, "fill": "yellow", "stroke": "green"}
    ret = Gauge(
        col=0,
        row=0,
        colSpan=colSpan,
        rowSpan=rowSpan,
        label="Employment Progress",
        **data
    )
    return ret


if __name__ == "__main__":

    widgets = [
        [[intro()], [toc()]],
        [[overview(), weapons()], [attributes(), awards()], [employment_progress()]],
        [[processes_table()]],
        [[skills_bar_chart()], [skills_other_bar_chart()]],
        [[languages_donuts()], [languages_table()]],
        [[professional_experience()], [other_experience()]],
        # [[exp_travis(), exp_travis_details()], [exp_travis_tldr()]],
        [[exp_travis(), exp_travis_details()], [exp_travis_tldr()]],
        [[exp_gandi(), exp_gandi_details()], [exp_gandi_tldr()]],
        [[looking_for()]],
        [[contact()]],
        # [[other_experience()]],
        # [[skills_stacked_chart()]], # stacked bar chart, doesn't work
        # [[skills_line_chart()]], # dumb line graph thing
    ]

    pages = {}
    i = 0
    for page in widgets:
        pages[i] = Page()
        row_y = 0

        for row in page:
            col_x = 0
            for widget in row:
                from IPython import embed

                # embed()
                widget.col = col_x
                widget.row = row_y
                pages[i].add_widget(widget)
                col_x = col_x + widget.colSpan
            row_y = row_y + widget.rowSpan
        i += 1

    doc = Document(pages)
    print(doc.content.encode("utf-8"))
