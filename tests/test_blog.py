import pytest

from pages.blog import blog

@pytest.mark.smoke
def test_customeapp(page):
    bl=blog(page)
    bl.blog_option_clicking()