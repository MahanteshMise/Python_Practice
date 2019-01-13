def anagram_test(a, b):
    x_temp = ''.join(sorted(a.replace(' ', '').lower()))
    y_temp = ''.join(sorted(b.replace(' ', '').lower()))

    if  x_temp == y_temp:
        return True
    return False


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal


class AnagramTest(object):

    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print('ALL TEST CASES PASSED')


# Run Tests
t = AnagramTest()
t.test(anagram_test)
