import os
import sys
import shutil

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

with open("gallery/index.html", "wb") as fh:
    template = env.get_template('index.html')
    themes = []
    for theme_dir in os.walk(sys.argv[1]).next()[1]:
        if theme_dir == ".git":
            continue
        theme = {}
        theme['name'] = theme_dir
        theme['path'] = '/' + theme_dir

        try:
            screenshot = sys.argv[1] + theme_dir + '/' + 'screenshot.png'
            thumbnail = 'gallery/' + 'thumbnails/' + theme_dir + '.png'
            shutil.copy(screenshot, thumbnail)
            theme['thumbnail'] = '/' + thumbnail
        except IOError as e:
            theme['thumbnail'] = None
            print e

        themes.append(theme)
    context = {
        'themes': themes
    }
    fh.write(template.render(**context))
