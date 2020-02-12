import unittest

class TestFindIP(unittest.TestCase):

    def test_Find_IP(self):
        result = find_ip.FindIP.run('192.0.2.0')
        self.assertEqual('192.0.2.0')
