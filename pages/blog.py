
class blog:
    def __init__(self,page):
        self.page=page
        self.b1=page.locator('a[href*="blog"]').filter(has_text="Blog").nth(0)

    def blog_option_clicking(self):
        self.b1.click()
        self.page.wait_for_load_state("load")
        self.page.go_back()

