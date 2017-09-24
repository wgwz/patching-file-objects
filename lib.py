import unittest
from unittest.mock import patch, mock_open

def get(file):
    with open(file, 'r') as f:
        return f.readlines() 

class TestLib(unittest.TestCase):
    
    @patch('__main__.open', mock_open(read_data='foo\nbar\nbaz\n'))
    def test_get_function(self):
        assert get('/path/to/file') == ['foo\n', 'bar\n', 'baz\n']

if __name__ == '__main__':
    unittest.main()
