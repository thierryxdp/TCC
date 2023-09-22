def posLetra(frase,letra,numero):
    '''Função que recebe uma frase, uma letra e um numero de sequencia dessa letra, retornando a posição da letra indicada na frase
str,str,int -> int '''
    if frase.count(letra)<i:
        return -1
    contador = 0
    extencao = len(frase)
    atual = 0
    while contador < extencao and atual < numero:
        if frase[contador] == letra:
            atual = contador
        contador = contador + 1
    return atual