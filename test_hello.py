import sys
from cStringIO import StringIO
import helloworld

class PatchStdin(object):
    def __init__(self, value):
        self._value = value
        self._stdin = sys.stdin
    def __enter__(self):
        # Monkey-patch stdin
        sys.stdin = StringIO(self._value)
        return self
    def __exit__(self, typ, val, traceback):
        # Undo the monkey-patch
        sys.stdin = self._stdin

def test_helloworld():
    # Usage
    with PatchStdin('1'):
        helloworld.helloworld()
    with PatchStdin('2'):
        helloworld.helloworld()
    with PatchStdin('3'):
        helloworld.helloworld()
    assert True == True