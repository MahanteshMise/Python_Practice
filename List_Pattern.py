def pair_sum(a, m):
    a = list(set(a))
    b = []
    counter = 0
    for i in range(len(a)):
        k = i
        for j in range(k+1, len(a)):
            s = a[k] + a[j]
            if a[k]+a[j] == m:

                b.append((a[k], a[j]))
                counter += 1
    return counter


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal


class TestPair(object):

    def test(self, sol):
        assert_equal(sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        assert_equal(sol([1, 2, 3, 1], 3), 1)
        assert_equal(sol([1, 3, 2, 2], 4), 2)
        print('ALL TEST CASES PASSED')


# Run tests
t = TestPair()
t.test(pair_sum)



