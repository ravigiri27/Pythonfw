
class contactus:
    def __init__(self,page):
        self.page=page
         #click on Contact Us 
        # self.c1=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
        self.c2=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
        self.c3=page.locator('(//input[@placeholder="Your Name"])[2]')
        self.c4=page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.c5=page.locator('(//input[@placeholder="Your Company"])[2]')
        self.c6=page.locator('(//select[@name="service"])[2]')
        self.c7=page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.c8=page.locator('(//textarea[@placeholder="Message"])[2]')
        self.c9=page.locator('(//input[@type="submit"])[2]')
        # self_contactus_option=[self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9]

    def contact_us_option(self):
        self.c2.click()
        self.c3.fill("Ravi")
        self.c4.fill("abc@xyz.com")
        self.c5.fill("uncodemy")
        self.c6.select_option("Web Development")
        self.c7.fill("456456454")
        self.c8.fill("Hello")
        self.c9.click()
       
