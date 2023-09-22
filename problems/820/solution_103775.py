def posLetra(frase,letra,num_ocorrencia):
    '''Função que, dada uma letra, procura-se a ocorrência
    de número dado (num_ocorrencia) numa determinada frase
    str, str, int -> int'''
    ocorrencias = []
    for c in enumerate(frase):
        if c[1] == letra:
            ocorrencias.append(c[0])
    if num_ocorrencia >= len(ocorrencias):
            return -1
    return ocorrencias[num_ocorrencia - 1]