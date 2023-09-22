def uppCons(x):
    for l in x:
        if l in 'qwrtypsdfghjklzxcvbnm':
            return str.upper(x)