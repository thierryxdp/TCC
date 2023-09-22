def posLetra(frase,letra, num):
    '''função que, dada uma frase(string), uma letra e um número que indica
    a ocorrencia desejada,retorna o indice da posição dessa ocorrencia.
    str,str,int-->int'''
    i=0
    posicao=-1
    while i<len(frase) and str.count(frase,letra)>=num:
        if frase[i]==letra:
            posicao= str.index(frase,letra,i)
        i=i+1
    return posicao