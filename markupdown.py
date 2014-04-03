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
