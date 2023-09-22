def posLetra(frase,letra,numero):
    '''função que indica a ocorrência de uma 
    letra fornecida em determinada frase
    valor de entrada: str, str, int
    valor de saída: int'''
    contador=0
    letras=[]
    fraselista=list(frase)
    if frase.count(letra)<numero:
        return -1
    else:
        while contador<len(fraselista) and len(letras)<numero:
            if letra==fraselista[i]:
                letras.append(fraselista[i])
            contador=contador+1
    return contador-1