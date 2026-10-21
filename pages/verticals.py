class verticals:
    def __init__(self,page):
        self.page=page
        self.Ver=page.locator("a[href='#']").filter(has_text="Verticals").nth(0)

        #trading option menu locators
        self.tr=page.locator("a[href='#']").filter(has_text="Trading").nth(0)
        self.tr1=page.locator("a[href*='stock-trading-mobile-app-development-company']").nth(0)
        self.tr2=page.locator("a[href*='paper-trading-app-development-company']").nth(0)
        self.tr3=page.locator("a[href*='cfd-trading-app-development-company']").nth(0)
        self.tr4=page.locator("a[href*='stock-trading-development-in-massachusetts']").nth(0)
        self.tr5=page.locator("a[href*='algo-trading-app-development-company']").nth(0)
        self.tr6=page.locator("a[href*='custom-trading-software-development-company']").nth(0)
        self.tr7=page.locator("a[href*='webportal-trading-development']").nth(0)

        self.trading_option=[self.tr,self.tr1,self.tr2,self.tr3,self.tr4,self.tr5,self.tr6,self.tr7]

        #Retail and Ecommerce option locatores
        self.rc=page.locator("a[href*='ecommerce-web-development-company']").nth(0)
        self.rc1=page.locator("a[href*='ecommerce-app-development']").nth(0)
        
        self.rc2=self.rc1
        self.retail_option=[self.rc,self.rc1,self.rc2]

        #Healthcare option locators
        self.hc=page.locator("a[href*='healthcare-mobile-app-development-company']").nth(0)
        self.hc1=page.locator("a[href*='diet-and-nutrition-app-developement']").nth(0)
        self.hc2=page.locator("a[href*='health-tracking-app']").nth(0)
        self.hc_option=[self.hc,self.hc1,self.hc2]

        #Fintech option locators
        self.ft=page.locator("a[href*='fintech-mobile-app-development-company']").nth(0)
        self.ft1=page.locator("a[href*='pos-software-development-company']").nth(0)
        self.ft2=page.locator("a[href*='cryptocurrency-mobile-app-development-company']").nth(0)
        self.ft_optopn=[self.ft,self.ft1,self.ft2]

        #Custom App option locators
        self.ca=page.locator("a[href='#']").filter(has_text="Custom App").nth(0)
        self.ca1=page.locator("a[href*='desktop-application-development-company']").nth(0)
        self.ca2=page.locator("a[href*='hrm-application-development-company']").nth(0)
        self.ca3=page.locator("a[href*='travel-mobile-app-development-company']").nth(0)
        self.ca4=page.locator("a[href*='dating-app-development-company']").nth(0)
        self.ca5=page.locator("a[href*='custom-crm-development-company']").nth(0)
        self.ca6=page.locator("a[href*='erp-app-development-company']").nth(0)
        self.ca7=page.locator("a[href*='e-learning-mobile-app-development-company']").nth(0)
        self.ca8=page.locator("a[href*='real-estate-mobile-app-development-company']").nth(0)
        self.ca_option=[self.ca,self.ca1,self.ca2,self.ca3,self.ca4,self.ca5,self.ca6,self.ca7,self.ca8]

    def trading_options_clicking(self):
        for i in self.trading_option:
            self.Ver.hover()
            self.tr.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def retail_option_clicking(self):
        for i in self.retail_option:
            self.Ver.hover()
            self.rc.hover()
            i.click()
            self.page.screenshot(path=r"C:\Users\Sangeeta\Desktop\playwright\screenshot\sc1.png")
            self.page.screenshot(path=r"C:\Users\Sangeeta\Desktop\playwright\screenshot\sc2.png")
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def healthcare_option_clicking(self):
        for i in self.hc_option:
            self.Ver.hover()
            self.hc.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def fintech_option_clicking(self):
        for i in self.ft_optopn:
            self.Ver.hover()
            self.ft.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def customeapp_option_clicking(self):
        for i in self.ca_option:
            self.Ver.hover()
            self.ca.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

                       
