
def string_compression1(seq):
    if len(seq) == 0:
        return ''
    seq = seq + '##'
    d = {}
    counter = 0
    for i in range(len(seq)-2):
        if seq[i] == seq[i+1]:
            counter += 1
        else:
            counter += 1
            d[seq[i]] = counter
            counter = 0
    s = ''.join(d)
    print(s)

def string_compression2(seq):
    if len(seq) == 0:
        return ''
    seq = seq + '##'
    d = []
    counter = 0
    for i in range(len(seq)-2):
        if seq[i] == seq[i+1]:
            counter += 1
        else:
            counter += 1
            # d[seq[i]] = counter
            d.append(seq[i])
            d.append(str(counter))
            counter = 0
    # print(d)
    return ''.join(d)
    

string_compression1('AAAAABBBBCCCC')
string_compression2('AAAAABBBBCCCC')

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print ('ALL TEST CASES PASSED')

# Run Tests
t = TestCompress()
t.test(string_compression2)