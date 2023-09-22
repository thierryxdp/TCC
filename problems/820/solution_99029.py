def posLetra(frase,letra,ocorrencia):
    """funcao que retorna o indice, no qual a letra de entrada aparece, segundo a ocorrencia informada, na frase;
    str, str, int -> int"""
    i=0
    numero_de_ocorrencias=0
    if str.count(frase,letra)<ocorrencia:
        return -1
    else:
        while i<len(frase):
            if frase[i]==letra:
                numero_de_ocorrencias=numero_de_ocorrencias+1
                i=i+1
            else:
                i=i+1
        return numero_de_ocorrencias