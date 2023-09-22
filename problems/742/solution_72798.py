def substitui(s,x,i):
    '''string, int, int -> string'''
    s*[i] = x
    return str1[0:i] + x + str1[i + 1:]