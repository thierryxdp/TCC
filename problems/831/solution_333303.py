def lingua_p(palavra):
    var = 'palavra'
    n = len('palavra')
    for i in range(1,n+1):
        if var[i] in 'aeiouAEIOU':
            var[i] = str(var[i])+'p'+str(var[i])
    return(var)