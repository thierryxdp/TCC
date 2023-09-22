def posLetra(frase,letra,n):
    ''' '''
    contagem_ocorre= str.count(frase,letra)
    ocorrencia=str.find(frase,letra)
    if contagem_ocorre < n:
        return -1
    return ocorrencia