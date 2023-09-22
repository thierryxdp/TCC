def posLetra(string, letra, numero):
    '''Esta função retorna em que posição da string aquela ocorrencia 
    de letra está. Caso exista menos ocorrenciass da letra do que a 
    ocorrencia pedida, a função deve retornar -1.
    str, str, int >>>  '''
    ocorrencias = 0
    i = 0
    
    while i < len(string):
        if string[i] == letra:
            ocorrencias += 1
        i += 1
        if ocorrencias == numero:
            return i