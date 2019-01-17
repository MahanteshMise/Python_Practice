def unique_character(arr):

    if len(arr) == 0:
        return True

    if len(arr) == 1:
        return True

    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            return False
    return True


"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')


# Run Tests
t = TestUnique()
t.test(unique_character)

