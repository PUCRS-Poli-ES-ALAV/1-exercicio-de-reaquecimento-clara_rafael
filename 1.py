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
    if n == 1:
        return 1
    if n == 2:
        
    return 

if __name__ == '__main__':
    #print(_1i(6, 4))
    # print(_1ii(3,2))
    #print(_1iii(3))
    print(_1iv('abc'))
