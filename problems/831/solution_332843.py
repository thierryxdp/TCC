def lingua_p(s):
    r = []
    for i in s:
        if i in ('a', 'e', 'i', 'o', 'u'):
        	l = str.partition(s, i)
    l = list(l)
    return l