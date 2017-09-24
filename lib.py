import unittest
from unittest.mock import patch, mock_open
import io 

# http://www.voidspace.org.uk/python/mock/helpers.html#mock-open
# https://stackoverflow.com/a/38454455
# https://stackoverflow.com/q/30329114
# https://stackoverflow.com/a/40405086/4028706

def get(file):
    with open(file, 'r') as f:
        return f.readlines() 

def set(file, line):
    with open(file, 'w') as f:
        return f.write(line)

class TestLib(unittest.TestCase):
    
    @patch('__main__.open', mock_open(read_data='foo\nbar\nbaz\n'))
    def test_get_function(self):
        assert get('/path/to/file') == ['foo\n', 'bar\n', 'baz\n']
    
    @patch('__main__.open', mock_open())
    def test_set_function_called_with_proper_args(self):
        set('/path/to/file', 'helloworld\n')
        open.assert_called_once_with('/path/to/file', 'w')

    @patch('__main__.open', mock_open())
    def test_set_function_write_called_with_proper_args(self):
        set('/path/to/file', 'helloworld\n')
        handle = open()
        handle.write.assert_called_once_with('helloworld\n')

if __name__ == '__main__':
    unittest.main()
