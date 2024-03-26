import unittest

from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome('a')
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = is_palindrome('aa')
        self.assertEqual(resultado, True)

    def test_ab(self):
        resultado = is_palindrome('ab')
        self.assertEqual(resultado, False)
    
    def test_asdfasdf(self):
        resultado = is_palindrome('asdfasdf')
        self.assertEqual(resultado, False)

    def test_neuquen(self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)

    def test_ABBA(self):
        resultado = is_palindrome('  ABBA')
        self.assertEqual(resultado, True)

    def test_123321(self):
        resultado = is_palindrome('123 32 1')
        self.assertEqual(resultado, True)

    def test_palindrome(self):
        resultado = is_palindrome('Neuq ueN')
        self.assertEqual(resultado, True)

    def test_palindrome2(self):
        resultado = is_palindrome('abca')
        self.assertEqual(resultado, False)

if __name__ == "__main__":
    unittest.main()