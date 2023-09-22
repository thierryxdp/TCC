def posLetra(palavra,letra,n):
    '''Função que recebe como entrada uma string,
    uma letra e um numero e retorna a posição da string que
    aquela ocorrencia esta'''
    if n > str.count(palavra,letra):
        return 'não existem tantas ocorrências'
    i = 1
    ind = str.index(palavra,letra)
    while i < n :
        i = 1 + i
        ind = str.index(palavra[ind+1:], letra) + len(palavra[:ind+1])
    return ind