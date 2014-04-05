# Markupdown: A simple API for converting between HTML and Markdown

## Overview

Markupdown is a simple REST based API for converting between Markdown,
HTML and then back again. It currently lives at:

    [http://markupdown.herokuapp.com](http://markupdown.herokuapp.com)

## Usage

### POST /md

This call takes a single parameter, `html` and attempts to convert it to [Markdown](http://daringfireball.net/projects/markdown/).

### POST /html

This call takes a single parameter, `md` and attempts to render it as HTML.

## Caveats and bugs

* The returned output doesn't have the correct Content-Type.
* There's more or less no attempt at error checking. Invalid input probably
  just crashes.

## License

Copyright (C) 2014, Andrew Gwozdziewycz. Licensed under the GPLv3.

### html2text.py

Copyright (C) 2004-2008 Aaron Swartz. GNU GPL 3.
