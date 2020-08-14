from abc import ABC,abstractmethod


class WebDriver(ABC):

    @abstractmethod
    def click(self):
        None


# w1=WebDriver() #Cannot create object of abstract class

class ChromeDriver(WebDriver):
    def click(self):
        print("Inside ChromeDriver Class")

class FirefoxDriver(WebDriver):
    def click(self):
        print("Inside Firefox Class")

w1=ChromeDriver()
w1.click()
