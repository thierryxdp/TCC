def uppCons(frase):
    '''função que recebe como entrada uma frase e retorne a frase com todas as suas consoantes em maiúsculas.
    entrada: str
    saída: str'''
    proximo = 0
    var1 = list(frase)
    acumulador = ''
    while proximo < len(var1):
        if var1[proximo] not in 'AEIOUaeiouáéíóúã':
            var1[proximo] = str.upper(var1[proximo])
        acumulador = acumulador +  var1[proximo]
        proximo = proximo + 1
    return acumulador