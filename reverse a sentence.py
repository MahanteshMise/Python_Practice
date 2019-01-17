def rev_word(sen):

    sen = sen.strip()
    sen = sen.split()
    a = []
    for i in range(len(sen)-1, -1, -1):
        a.append(sen[i])
    return " ".join(a)


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal


class ReversalTest(object):

    def test(self, sol):
        assert_equal(sol('    space before'), 'before space')
        assert_equal(sol('space after     '), 'after space')
        assert_equal(sol('   Hello John    how are you   '), 'you are how John Hello')
        assert_equal(sol('1'), '1')
        print("ALL TEST CASES PASSED")


# Run and test
t = ReversalTest()
t.test(rev_word)

#reverse_sentence("hello    this    is mahantesh  ")

