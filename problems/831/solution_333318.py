def lingua_p(palavra):
    var = 'palavra'
    n = len('palavra')
    for i in range(1,n+1):
        if var[i] in 'aeiou':
            var[i] = var[i]+str(p)+var[i]
    return(var)