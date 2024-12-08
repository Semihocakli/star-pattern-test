import unittest
from yildiz import yildiz_olustur

class YildizTestleri(unittest.TestCase):
    def test_yildiz_deseni_1(self):
        """5 satırlık yıldız desenini kontrol eder"""
        beklenen_sonuc = "*\n**\n***\n****\n*****"
        self.assertEqual(yildiz_olustur(5), beklenen_sonuc)
    
    def test_yildiz_deseni_2(self):
        """Farklı uzunluktaki yıldız desenlerini kontrol eder"""
        self.assertEqual(yildiz_olustur(1), "*")
        self.assertEqual(yildiz_olustur(3), "*\n**\n***")

if __name__ == '__main__':
    unittest.main()
