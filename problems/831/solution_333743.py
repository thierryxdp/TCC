def lingua_p(x):
    vogal = ('a','e','i','o','u')
    silaba = ()
    for n in x:
        if n in vogal:
            silaba = silaba + (n + 'p' + n, )
            return silaba