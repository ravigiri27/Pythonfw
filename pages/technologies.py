
class technologies:
    def __init__(self,page):
        self.page=page
        self.tech=page.locator("a[href='#']").filter(has_text="Technologies").nth(0)
        self.ecd=page.locator("a[href*='ecommerce-web-development-company']").nth(2)
        self.ecd1=page.locator("a[href*='magento-development']").nth(0)
        self.ecd2=page.locator("a[href*='opencart-development']").nth(0)
        self.ecd3=page.locator("a[href*='codeigniter-development']").nth(0)
        self.ecd4=page.locator("a[href*='wordpress-development']").nth(0)
        self.ecd5=page.locator("a[href*='big-commerce']").nth(0)
        self.ecd6=page.locator("a[href*='shopify-development']").nth(0)
        self.ecd7=page.locator("a[href*='cs-cart-development']").nth(0)
        self.ecd8=page.locator("a[href*='node-js-development']").nth(0)
        self.ecd9=page.locator("a[href*='nopcommerce-design-and-development-company']").nth(0)
        self.ecd10=page.locator("a[href*='woocommerce-development']").nth(0)
        self.ecd11=page.locator("a[href*='laravel-development']").nth(0)
        self.ecd12=page.locator("a[href*='prestashop-development']").nth(0)
        self.ecd13=page.locator("a[href*='drupal-development']").nth(0)
        self.ecd14=page.locator("a[href*='wix-development']").nth(0)
        self.ecd15=page.locator("a[href*='joomla-development']").nth(0)
        self.ecd16=page.locator("a[href*='react-js-development']").nth(0)
        self.ecd17=page.locator("a[href*='express-js-development']").nth(0)
        self.ecd_option=[self.tech,self.ecd1,self.ecd2,self.ecd3,self.ecd4,
                                     self.ecd5,self.ecd6,self.ecd7,self.ecd8,
                                     self.ecd9,self.ecd10,self.ecd11,self.ecd12,self.ecd13,self.ecd14,self.ecd15,self.ecd16,self.ecd17]

        #mobile app option locators
        self.ma=page.locator("a[href*='mobile-app-development-company']").nth(7)
        self.ma1=page.locator("a[href*='react-native-mobile-app-development']").nth(0)
        self.ma2=page.locator("a[href*='enterprise-mobile-app-development']").nth(0)
        self.ma3=page.locator("a[href*='xamarin-mobile-app-development']").nth(0)
        self.ma4=page.locator("a[href*='kotlin-mobile-app-development']").nth(0)
        self.ma5=page.locator("a[href*='flutter-mobile-app-development']").nth(0)
        self.ma6=page.locator("a[href*='ionic-mobile-app-development']").nth(0)
        self.ma7=page.locator("a[href*='swift-mobile-app-development']").nth(0)
        self.ma8=page.locator("a[href*='appointment-booking-development']").nth(0)
        self.ma_option=[self.ma,self.ma1,self.ma2,self.ma3,self.ma4,self.ma5,self.ma6,self.ma7,self.ma8]

        # No option under AI tab
        self.ai=page.locator("a[href*='artificial-intelligence-development-services-company-india']").filter(has_text="Artificial Intelligence").nth(0)

    def ecommercedev_option_clicking(self):
        for i in self.ecd_option:
            self.tech.hover()
            self.ecd.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def ma_option_clicking(self):
        for i in self.ma_option:
            self.tech.hover()
            self.ma.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def ai_option_clicking(self):
        self.tech.hover()
        self.ai.hover()
        self.ai.click()
        self.page.wait_for_load_state("load")