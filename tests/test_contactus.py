import pytest

from pages.contactus import contactus

@pytest.mark.smoke
def test_customeapp(page):
    bl=contactus(page)
    bl.contact_us_option()