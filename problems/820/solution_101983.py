def PosLetra(frase,letra,n):
    """ Função que identifica a posição da ocorrencia n de uma letra, dada uma frase qualquer
    str,str,int -> int """
    i=0
    listaletras=[]
    while i<len(frase):
        if frase[i] == letra:
            listaletras+=[str.index(frase[i])]
        i+=1
    return listaletras[n-1]