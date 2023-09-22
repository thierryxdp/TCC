def posLetra(texto,letra,n):
    """Função retorna, dada uma string, em que indice 
    ocorreu o aparecimento de um termo N, em função da ocorrencia
    determinada pelo valor n
        str,str,int->int"""
    i=0
    while i < len(texto):
        if letra in texto:
            frase=str.replace(texto,letra,'/',n-1)
        i=i+1

    if letra in frase:
        return frase.index(letra)
    else:
        return -1