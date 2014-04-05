# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from bottle import route, run, template, default_app, request
from html2text import html2text
from markdown import markdown

@route('/md', method='POST')
def md():
    html = request.POST.get('html', '')
    return html2text(html)

@route('/html', method='POST')
def html():
    md = request.POST.get('md', '')
    return markdown(md)

@route('/')
def index():
    return """<html><head><title>Markupdown</title></head><body>
<pre>
<strong>Markupdown</strong> Convert stuff between HTML and Markdown

- POST /md - Convert HTML to markdown

  parameters: `html`

- POST /html - Convert markdown to HTML

  parameters: `md`
</pre>
</body></html>"""

app = default_app()
