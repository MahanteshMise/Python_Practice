def print_count(arr):

    """Checking the edge condition"""
    if len(arr) == 0:
        return 0        #if the len of the array is equal to 0 return False

    max_sum = current_sum = arr[0]

    for i in arr[1:]:
        current_sum = max(current_sum+i, i)  # checking the max among the current_sum and the present number i
        max_sum = max(current_sum, max_sum)

    return max_sum

# Defining the test cases:

from nose.tools import assert_equal


class LargeContTest(object):
    def test(self, sol):
        assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
        assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        assert_equal(sol([-1, 1]), 1)
        print('ALL TEST CASES PASSED')


# Run Test
t = LargeContTest()
t.test(print_count)

