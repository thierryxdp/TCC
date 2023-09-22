def posLetra(frase,letra,n):
    '''Função que pega a frase de entrada conta quantas vezes a letra aparece, e retorna o numero de ocorrencias dessa letra
    	caso o numero de ocorrencias seja menor que valor n de entrada, retorna -1
        str,str→int'''
    contagem_ocorre= str.count(frase,letra)
    ocorrencia=str.find(frase,letra)
    if contagem_ocorre < n:
        return -1
    return ocorrencia