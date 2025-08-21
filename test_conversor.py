import unittest
from conversor import c_a_f # Importacion de la funcion

class TestConversion(unittest.TestCase):
    def test_0_celsius(self):
        self.assertEqual(c_a_f(0), 32)  # Test para 0°C
    
    def test_100_celsius(self):
        self.assertEqual(c_a_f(100), 212)  # Test para 100°C

if __name__ == '__main__':
    unittest.main()