def posLetra(frase,letra,ocorrencia):
    '''
    Função que recebe como entrada uma string, uma letra
    e um número que indica a ocorrência desejada da letra e
    retorna a posição de onde a letra está, caso a ocorrência
    pedida seja menor, a função retornará -1.
    
    str, str, int -> int
    '''
    if frase.count(letra) < ocorrencia:
        return -1
    cont = 1
    posi = frase.index(letra)
    while cont < ocorrencia:
        posi = frase.index(letra, posi + 1)
        cont = cont + 1
    return posi