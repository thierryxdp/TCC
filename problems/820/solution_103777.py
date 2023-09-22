def posLetra(frase,letra,num_ocorrencia):
    '''Função que, dada uma letra, procura-se a ocorrência
    de número dado (num_ocorrencia) numa determinada frase
    str, str, int -> int'''
    pos = frase.find(letra)
    while pos >= 0 and num_ocorrencia > 1:
        pos = frase.find(letra, pos + 1)
        num_ocorrencia -= 1
    return pos