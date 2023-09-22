def lingua_p(x):
    var = x
    n = len(x)
    for i in range(1,n+1):
        if var[i] = 'aeiou':
            var[i] = var[i]+'p'+var[i]
    return(var)