def posLetra(string, letra, ocorrencia):
    '''dada uma frase, retorna a posicao de dada ocorrencia de dada letra. caso a ocorrencia informada seja maior que o numero de ocorrencias totais, ira retornar -1
    str, str, int -> int'''
    cont_ocorrencia = 0
    for i in string:
        if i == letra:
            cont_ocorrencia += 1
    if ocorrencia > cont_ocorrencia:
        return -1
    else:
        return str.index(string, letra, ocorrencia)