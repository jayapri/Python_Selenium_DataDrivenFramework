import unittest
import XLgeneric
import HtmlTestRunner
from selenium import webdriver


class Testcase(unittest.TestCase):
    def test_Mumbai_bed(self):
        driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
        driver.implicitly_wait(10)
        path = "C://Users//Balak//Desktop//MissionHumaneTestCaseXL//TestCaseMumbaiBed.xlsx"
        driver.get("https://app.missionhumane.org/maharashtra/mumbai/bed/")
        test3 = driver.find_elements_by_xpath("//p[@class = 'MuiTypography-root card-desc MuiTypography-body2']")
        rows = 2
        for x in range(len(test3)):
            XLgeneric.writeData(path, "Sheet1", rows, 2, test3[x].text)
            rows = rows + 1
        rownum = 2
        for y in range(2, 302):
            compare1 = XLgeneric.readData(path, "Sheet1", rownum, 1)
            compare2 = XLgeneric.readData(path, "Sheet1", rownum, 2)
            if compare1 == compare2:
                XLgeneric.writeData(path, "Sheet1", rownum, 3, "passed")
            else:
                XLgeneric.writeData(path, "Sheet1", rownum, 3, "failed")
                self.assertEqual(compare1, compare2, "Both fields are not equal")
            rownum = rownum + 1


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C://Users//Balak//PycharmProjects//pythonSeleniumproject//Sample projects//Reports'))

