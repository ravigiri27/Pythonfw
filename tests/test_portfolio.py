
import pytest

from pages.portfolio import portfolio

@pytest.mark.smoke
def test_portfoliopage(page):
    p=portfolio(page)
    p.portfolio_option_clicking()
    p.view_more_clicking()