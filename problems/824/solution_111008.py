def uppCons(fra):
    '''Essa função recebe uma frase 'fra' em que cada elemento dela é
    atribuido a uma lista 'lis', dessa forma é possivel alterar seus 
    elementos, então é feito um while que percorre toda lis e a cada 
    iteração é verificado se é uma vogal, caso não seja aquela conçoante
    é colocada em maiúsculo, após isso é transformado essa lista em uma string
    string----->string'''
    i = 0
    lis = list(fra)
    vogais = "aeiouáéíóúÁÉÍÓÚAEIOUÃãõÕ"
    
    while i < len(fra):
        if lis[i] not in vogais:
            lis[i] = str.upper(lis[i])
            i += 1
        else:
            i += 1
    return str.join('', lis)