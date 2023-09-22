def faltante(lista):
    ''' a função recebe uma lista de tamanho (n-1) com numeros 
    inteiros não repetido e retorna o numero 
    que ta faltando na sequencia que pertece ao intervalo
    [1,N]
    list->int
    '''
    f=1
    proximo=0
    while f<len(lista)+1:
        if f!= lista[proximo] and f< len(lista)+1:
            return f 
        proximo= proximo+1
        f=f+1
    if f ==len(lista)+1:
        return f