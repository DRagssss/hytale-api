from .http import get
from .models.blogs.blog_post import BlogPost
from .models.blogs.blog_post_excerpt import BlogPostExcerpt


def get_blogs(limit=3) -> list[BlogPostExcerpt]:
    data = get("/blog/post/published", limit=limit)
    return [BlogPostExcerpt.from_dict(item) for item in data]


def get_blog(slug: str) -> BlogPost:
    data = get(f"/blog/post/slug/{slug}")
    return BlogPost.from_dict(data)


def get_blogs_time(year: int, month: int) -> list[BlogPostExcerpt]:
    data = get(f"/blog/post/archive/{year}/{month}")
    return [BlogPostExcerpt.from_dict(item) for item in data]
