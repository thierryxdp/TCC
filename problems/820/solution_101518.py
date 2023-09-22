def posLetra(frase, letra, numero):
    '''funcao que, dada uma frase, uma letra e um numero, retorna a posicao da letra na
    frase de acordo com a n-esima ocorrencia, a qual e indicada pelo numero. Caso o numero
    seja maior que a quantidade de ocorrencias, retorna -1;
    str,int,int->int'''
    indice = str.find(frase,letra)
    if numero>str.count(frase,letra):
        return -1
    while numero>0:
        indice = str.find(frase,letra,indice)
        indice = indice + 1
        numero = numero -1
    return indice - 1