def posLetra(frase,letra,numero):
    """Funcao que recebe uma frase,uma letra e um numero e retorna o indice da ocorrencia especifica daquela letra na posicao do numero dado;str,str->int"""
    i=0
    ocorrencias=0
    if str.count(frase,letra)<numero:
        return -1
    else:
        while ocorrencias<numero:
            if frase[i]==letra:
                ocorrencias=ocorrencias+1
            i=i+1
        return i-1