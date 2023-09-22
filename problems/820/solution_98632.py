def posLetra(frase,letra,ocorrencia):
    '''Função que recebe uma frase, uma letra e uma ocorrência quaisquer e retorna a posição da letra de acordo com a ocorrência fornecida. Caso existam menos ocorrências da letra do que a pedida, a função retorna -1.
str,str,int --> int'''
    lista = list(frase)
    if list.count(lista,letra) < ocorrencia:
        return -1
    i = 0
    cont = 0
    while cont < ocorrencia:
        if lista[i] != letra:
            i = i+1
        elif lista[i] == letra:
            cont = cont+1
            i = i+1
        if cont == ocorrencia:
            return i-1