
class socialmedia:
    def __init__(self, page):
        self.page = page
        self.about = page.locator('(//a[@href="https://www.tranktechnologies.com/about"])[1]')
        self.facebook = page.locator('//a[@href="https://www.facebook.com/TrankTechnologies"]')
        self.linkedin = page.locator('//a[@href="https://in.linkedin.com/company/trank-technologies-official"]')
        self.insta = page.locator('//a[@href="https://www.instagram.com/tranktechnologies/"]')
        self.pin = page.locator('//a[@href="https://in.pinterest.com/tranktechnologies12/"]')
        self.twitter = page.locator('//a[@href="https://twitter.com/tranktechno"]')
        self.youtube = page.locator('//a[@href="https://www.youtube.com/channel/UCWu1Y-tfrXf-Utpaft830Cg"]')
        self.quora = page.locator('//a[@href="https://www.quora.com/profile/Trank-Technologies-1"]')
        self.socialmediaList = [
            self.facebook,
            self.linkedin,
            self.insta,
            self.pin,
            self.twitter,
            self.youtube,
            self.quora,
        ]

    def _open_social_link(self, social_media_link):
        previous_url = self.page.url

        try:
            with self.page.context.expect_page(timeout=5000) as new_page_info:
                social_media_link.click()

            new_tab = new_page_info.value
            new_tab.wait_for_load_state("domcontentloaded")
            new_tab.close()
        except TimeoutError:
            self.page.wait_for_url(lambda url: url != previous_url, timeout=10000)
            self.page.go_back()
            self.page.wait_for_load_state("domcontentloaded")

    def socialmediapageclick(self):
        self.about.click()
        self.page.wait_for_load_state("domcontentloaded")

        for social_media_link in self.socialmediaList:
            self._open_social_link(social_media_link)