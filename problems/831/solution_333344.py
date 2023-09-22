def lingua_p(x):
    var = x
    n = len(x)
    for i in range(1,n+1):
        if var[i] in 'aeiou':
            var[i] = var[i] + str(p) + var[i]
    return(var)