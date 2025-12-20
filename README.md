# hytale-api

Unofficial Python library for interacting with the Hytale API.

⚠️ **This library is unofficial and based on publicly discovered endpoints.**

Hytale is set to release on the 13th of January and I hope more _documented_ and more useful endpoints can be added.

## Get Started

### Installation

```bash
pip install hytale-api
```

OR

```bash
pip install git+https://github.com/DRagssss/hytale-api.git
```

### Example Use

This package only consists of endpoint that do not need any authorization (since there is no official API documentation from Hypixel Studios yet) so it's extremely easy to use.

Get excerpts of the latest 3 blogs.

```Python
from hytale import get_blogs

blogs = get_blogs()  # limit defaults to 3

for blog in blogs:
    print(blog.bodyExcerpt)  # first couple sentences of body
```

You can also get the entire HTML body of a singular blog.

```Python
from hytale import get_blog

slug = "hytale-s-1st-faq"  # https://hytale.com/news/2025/12/hytale-s-1st-faq
blog = get_blog(slug)

print(blog.body)  # very long HTML content
```
