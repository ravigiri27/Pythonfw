import pytest

from pages.technologies import technologies

@pytest.mark.smoke
def test_customeapp(page):
    t1=technologies(page)
    t1.ecommercedev_option_clicking()

@pytest.mark.smoke
def test_mobile(page):
    t2=technologies(page)
    t2.ma_option_clicking()

@pytest.mark.smoke
def test_ai(page):
    t3=technologies(page)
    t3.ai_option_clicking()



