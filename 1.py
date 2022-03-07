def _1i(n,m):
    if not n:
        return 0
    return m + _1i(n-1, m)

def _1ii(n,m):
    if n > 1:
        return 1 + _1ii(n-1,m)
    if m > 1:
        return 1 + _1ii(n,m-1)
    return 2

def _1iii(n):
    if n == 1:
        return 1
    return 1/n + _1iii(n-1)

def _1iv(s):
    if len(s) == 0:
        return ''
    return s[len(s) - 1] + _1iv(s[:len(s) - 1])

def _1v(n):
    # ???
    if n == 1:
        return 1
    if n == 2:
        return 2
    return 2 * _1v(n-1) + 3 * _1v(n-2)

def _1vi(m,n):
    # ???
    if m == 0:
        return n + 1
    if m!= 0 and n ==0:
        return _1vi(m-1, 1)
    if m!=0 and n!=0:
        return _1vi(m-1, _1vi(m,n-1))

def _1vii(list):
    # ???
    if len(list) == 1:
        return list[0]
    r1 = list[0] + _1vii(list[1:])
    r2 = _1vii([list[0]]) * _1vii(list[1:])
    return r1, r2

def _1viii(s):
    if len(s) <= 1:
        return True
    # if s[::1] == s[::-1]:
    #     return True
    # else:
    #     return False
    if s[0] == s[-1]:
        return _1viii(s[1:-1])
    else:
        return False

def _1ix(n):
    # ????
    list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if n == 0:
        return ' '
    if n == 1:
        return list[0]
    return list[:n], list[n:1]

def _1x(n):
    # ???? funciona, mas é isso mesmo?
    if n <= 1:  
        return n  
    else:  
        return(_1x(n-1) + _1x(n-2))

if __name__ == '__main__':
    #print(_1i(6, 4))
    # print(_1ii(3,2))
    #print(_1iii(3))
    #print(_1iv('abc'))
    print(_1v(3))
    # print(_1vi(3,2))
    # print(_1vii([1,2,3,7]))
    # print(_1viii('aba'))
    # print(_1ix(4))
    # print(_1x(2))