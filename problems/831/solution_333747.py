def lingua_p(x):
    vogal = ('a','e','i','o','u')
    silaba = ()
    for n in x:
        if n in vogal:
            silaba = silaba + (n + 'p' + n, )
    for j in x:
        if j in vogal:
            else:
                return j == silaba.index[0]