import unittest
import scrapping
# , “ritvik.jain.52206 “”, “”, “”
class test_scrap(unittest.TestCase) :
    def test_1(self) :
        uname = 'rishi.ranjan.54966'
        self.assertEqual(scrapping.srch_name(uname), "Rishi Ranjan")
        self.assertEqual(scrapping.srch_city(uname), "Patna, India")
        self.assertEqual(str(scrapping.srch_work(uname)), "['École Polytechnique Fédérale de Lausanne']")

    def test_2(self) :
        uname = 'utkarsh.parkhi.1'
        self.assertEqual(scrapping.srch_name(uname), "Utkarsh Parkhi")
        self.assertEqual(scrapping.srch_city(uname), "Roorkee")
        self.assertEqual(str(scrapping.srch_work(uname)), "['IMG, IIT Roorkee']")








if __name__ == '__main__' :
    unittest.main()