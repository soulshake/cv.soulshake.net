#!/usr/bin/env python
# -*- coding: utf-8 -*-
# how would i describe myself: http://bashooka.com/inspiration/30-great-examples-of-creative-cv-resume-design/
import snippets
from snippets import *
import click
from tabulate import tabulate

def contact_info():
    # Is this thing on?
    # blog, twitter, email, current location
    pass

def awards():
    # 10th grade hardest worker at track ^_^
    pass

def things_i_love():
    # things i love entirely too much
    # hat tip to Norman Veilleux/Ryan Harding for the heart
    heart = """
    Things I love entirely too much:

      .....           .....
  ,ad8PPPP88b,     ,d88PPPP8ba,
 d8P"      "Y8b, ,d8P"      "Y8b
dP'           "8a8"           `Yd
8(   APIs       "    CLIs      )8
I8                             8I
 Yb,   humans     squirrels  ,dP
  "8a,                     ,a8"
    "8a,     ASCII       ,a8"
      "Yba     (obvs)  adP"
        'Y8a         a8P'
          '88,     ,88'
            "8b   d8"
             "8b d8"
              '888'
                "
    """
    heart = click.style(heart, fg='red')
    heart += click.style("\n JK. One can never love these things too much.", dim=True)
    ret = Markdown(colSpan=3, rowSpan=7, data=heart, col=0, row=0)
    return ret

def skills_line_chart():
    # abilities vs interests

    skills = LineChart(xPadding=5, col=0, row=0, colSpan=8, rowSpan=10)
    skills.add_line(title="social media",
                    style_line="yellow",
                    x="2011,2012,2013,2014,2015,2016,2017",
                    y="30,50,40,40,30,40,50",
                    )
    skills.add_line(title="development",
                    style_line="green",
                    x="09:00,09:05,09:10,09:15,09:20,09:25,09:30",
                    y="10,30,20,30,25, 10"
                    )

    skills.add_line(title="mraaaaaa",
                    style_line="blue",
                    x="09:00,09:05,09:10,09:15,09:20,09:25,09:30",
                    y="20,40,50,10,50,50,60",
                    )
    return skills


def skills_bar_chart():
    barchart = BarChart(col=1, row=1, colSpan=4, rowSpan=4)
    skill_names = ["Python", "bash", "GoLang", "DNS", "Docker"]
    skill_levels = [7, 4, 2, 5, 5]

    chart_attributes = {
        "barWidth": 4,
        "barSpacing": 15,
        "xOffset": 10,
        "maxHeight": 5,
        "height": "100%",
        "border_type": "line",
        "border_fg": "gray",
        "data_titles": skill_names,
        "data_data": skill_levels,
        }

    barchart.add_bar(title="Python", data=5)
    barchart.add_bar(title="bash", data=4)
    barchart.add_bar(title="GoLang", data=2)
    barchart.add_bar(title="DNS", data=4)
    barchart.add_bar(title="Docker", data=3)
    barchart.add_bar(title="Linux", data=3)
    return barchart

def languages_table():
    languages = Table(col=2, row=2, colSpan=4, rowSpan=3)
    languages.add_columns(["Language", "time", "DuoLingo level", "ease", "status"])
    rows = [
            ["English", ">10y", 99, "99%", "{green-fg} native speaker"],
            ["French", ">10y", 82, "89%", "{green-fg} fluent"],
            ["German", "2 mo", 18, "39%", "{yellow-fg} rather clumsy"],
            ["Spanish", "n/a", 17, "29%", "{blue-fg} passive"],
            ["Russian", "1 mo", 11, "15%", "{red-fg} caveperson"],
            ["Arabic", "n/a", 8, "3%", "{red-fg} don't ask"],
            ]
    for row in rows:
        languages.add_row(row)
    return languages

def about_me():
    about_me = ([
              "My name is AJ, and I like to code.",
              "",
              "Say hi:",
                "- [https://github.com/soulshake](https://github.com/soulshake) ",
                "- [https://twitter.com/s0ulshake](https://twitter.com/s0ulshake)",
                "- [aj@soulshake.net](aj@soulshake.net)",
                "- [https://www.linkedin.com/in/ajbowen](https://www.linkedin.com/in/ajbowen)",
                "",
              "For more info, see http://blog.soulshake.net/2016/04/command-line-resume/",
              ])

    about_me = "\n".join(about_me)
    about = Markdown(colSpan=6, rowSpan=4, data=about_me, col=3, row=3)
    return about

def experience():
    blurb = [click.style("# Experience", bold=True, fg="green")]
    blurb += """
----------
## **Chief of Counter-bullshit operations, Gandi.net** (February 2012 to December 2015, San Francisco)

AKA developer advocate, technical community manager, support automation specialist, chaos monkey

I interacted with various tech communities, online and at industry events, letting developers know we exist, helping them make the most of Gandi's domain, SSL and hosting APIs, and communicating their feedback to our technical team. Internally, I worked with engineers, product managers and support to improve Gandi's APIs, web interface, documentation and open source presence.

Job responsibilities included:

* **Special projects**: being ready for anything that comes up
* **Outreach**, both online and in person (at tech conferences and industry events), helping existing and prospective customers to make the most of Gandi's products (domain names, SSL certs, hosting, and the corresponding APIs);
* **Localization**: technical and marketing communications (product releases, newsletters, announcement, outages);
* **Documentation**: creating and editing tutorials and docs
* **Communication**: Helping shape Gandi's voice our blog posts, newsletters and social media interactions, organize events and manage our supported projects.
* **Community**: Cultivating a [thriving and enthusiastic community](https://twitter.com/gandibar/favorites).
* **Social media**: managing Gandi's presence (initially a French brand) on US and English-speaking channels;

## **Support representative, Gandi.net**

My original role at Gandi was entry-level support: troubleshooting and explaining issues relating to domain names, DNS, SSL certificates and basic hosting. My curiosity and interest in this role led me to specialize in more technical hosting issues, while helping to hire, train and mentor new employees. My French language and community-related skills led me to move to San Francisco to take on an official evangelism role in 2013.

**Previous positions**: See LinkedIn profile
        """.split("\n")
    blurb = Markdown(colSpan=8, rowSpan=11, data=blurb, col=0, row=0)
    return blurb

def spedometer():
    ret = Spedometer().content
    ret = Markdown(colSpan=5, rowSpan=5, data=ret, col=0, row=0)
    return ret

def toc():

    ret = [
        ".",
        u"╒══════════════════ Welcome to the professional resume of A.J. Bowen ══════════════════════╕",
        u"│                                                                                          │",
        u"│  0. This screen                                                                          │",
        u"│  1. Skills                                                                               │",
        u"│  2. Experience                                                                           │",
        u"│  3. Languages                                                                            │",
        u"│  4. About me                                                                             │",
        u"│                                                                                          │",
        u"│  To view all slides (press enter to move to next slide; press Ctrl+C to exit)            │",
        u"│                                                                                          │",
        u"│    $ p=0; while true; do curl localhost/$((p++))\?cols=$((COLUMNS)); read; done          │",
        u"│                                                                                          │",
        u"│  To view a specific slide:                                                               │",
        u"│                                                                                          │",
        u"│    $ curl -N cv.soulshake/3                                                              │",
        u"│                                                                                          │",
        u"│  Options (URL paramters):                                                                │",
        u"│                                                                                          │",
        u"│   \?auto                 Advance through slides automatically (5 seconds each)           │",
        u"│   \&cols=$((COLUMNS))    Specify number of rows                                          │",
        u"│   \&rows=$((LINES))      Specify number of columns                                       │",
        u"│   \&terminal=xterm       Specify your terminal                                           │",
        u"│                                                                                          │",
        u"│  You can infer them automatically from your environment:                                 │",
        u"│                                                                                          │",
        u"│    $ curl -N cv.soulshake.net\?\&cols=$((COLUMNS))\&rows=$((LINES-5))\&terminal=${TERM}  │",
        u"│                                                                                          │",
        u"│                                                                                          │",
        u"╘══════════════════════════════════════════════════════════════════════════════════════════╛"]

    ret = Markdown(data=ret)
    return ret

def title(text, **kwargs):
    title = "\n".join(ret)
    ret = Markdown(colSpan=8, rowSpan=6, data=ret, col=0, row=0)
    
if __name__ == "__main__":

    #languages_title = title("Human languages")

    spedometer = spedometer()
    #spedometer.auto_adjust()
    toc = toc()
    skills = skills_line_chart()
    about = about_me()
    languages = languages_table()
    #languages.auto_adjust()
    #import ipdb; ipdb.set_trace()

    more_skills = skills_bar_chart()
    experience = experience()
    love = things_i_love()

    # Specify which page/toc
    widgets = {
        0: [[toc]],
        1: [[spedometer]],
        2: [[languages]],
        3: [[more_skills]],
        4: [[experience]],
        5: [[about]],
        6: [[love]],
        7: [[skills]],
    }

    pages = {}
    for i in widgets:
        pages[i] = Page()
        x = 0
        y = 0
        for row in widgets[i]:
            x = 0
            for widget in row:
                #x = 0
                widget.col = x
                widget.row = y
                pages[i].add_widget(widget)
                x = x + widget.colSpan
            y = y + widget.rowSpan

    doc = Document(pages)
    print(doc.content).encode('utf-8')

