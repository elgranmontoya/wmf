# Wikimedia Foundation Tools

This project is a collection of tools that's useful for integrating with different APIs at WMF.  To start, it supports the Analytics pageview API.

## Analytics - pageview API

Install with pip: `pip install wmf`

And use:

```
from wmf.analytics.api import PageviewsClient

p = PageviewsClient()

p.article_views('en.wikipedia', ['Selfie', 'Cat', 'Dog'])
p.project_views(['ro.wikipedia', 'de.wikipedia', 'commons.wikimedia'])
p.top_articles('en.wikipedia', limit=10)
```
