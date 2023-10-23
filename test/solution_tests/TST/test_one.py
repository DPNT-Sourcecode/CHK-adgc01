import sys
sys.path.append(1, '')
from solutions.TST import one


class TestSum():
    def test_sum(self):
        assert one.get() == 1
