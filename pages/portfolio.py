class portfolio:
    def __init__(self, page):
        self.page = page
        self.p1 = page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]')
        self.view_more_links = page.get_by_role("link", name="View More", exact=True)

    def portfolio_option_clicking(self):
        self.p1.click()
        self.page.wait_for_load_state("load")

    def view_more_clicking(self):
        for index in range(self.view_more_links.count()):
            link = self.view_more_links.nth(index)
            with self.page.context.expect_page(timeout=10000) as new_page_info:
                link.click(modifiers=["Control"])

            new_tab = new_page_info.value
            try:
                new_tab.wait_for_load_state("domcontentloaded", timeout=15000)
            finally:
                new_tab.close()
