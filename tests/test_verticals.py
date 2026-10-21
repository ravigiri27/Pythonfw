
import pytest

from pages.verticals import verticals

@pytest.mark.smoke
def test_trading(page):
    obj=verticals(page)
    obj.trading_options_clicking()

@pytest.mark.smoke
def test_retail(page):
    obj1=verticals(page)
    obj1.retail_option_clicking()

@pytest.mark.smoke
def test_healthcare(page):
    obj2=verticals(page)
    obj2.healthcare_option_clicking()

@pytest.mark.smoke
def test_fintech(page):
    obj3=verticals(page)
    obj3.fintech_option_clicking()

@pytest.mark.smoke
def test_customeapp(page):
    obj4=verticals(page)
    obj4.customeapp_option_clicking()


                