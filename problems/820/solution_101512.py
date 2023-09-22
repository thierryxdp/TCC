def posLetra(frase, letra, numero):
    '''funcao que, dada uma frase, uma letra e um numero, retorna a posicao da letra na
    frase de acordo com a n-esima ocorrencia, a qual e indicada pelo numero. Caso o numero
    seja maior que a quantidade de ocorrencias, retorna -1;
    str,int,int->int'''
    indice = str.find(frase,letra)
    if numero>str.count(frase,letra):
        return -1
    while indice>=0 and numero>1:
        indice = str.find(frase,letra,numero + 1)
        numero=0
    return indice