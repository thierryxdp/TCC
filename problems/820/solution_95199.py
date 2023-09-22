def posLetra(string, letra, numero):
    """A função recebe uma string, uma letra e um número que indica a 
    ocorrência desejada da letra, e retorna qual a indexação da ocorrência
    definida;
    str, str, int -> int"""
    indexacao = 0
    indexacao_ocorrencia = 0
    i = 0
    if numero>str.count(string, letra):
        return -1
    while i<len(string):
        if string[i] == letra and indexacao_ocorrencia<numero:
            indexacao_ocorrencia = indexacao_ocorrencia + 1
        i = i + 1
        if string[i] != letra and indexacao_ocorrencia<numero:
            indexacao = indexacao + 1
        i = i + 1
    return indexacao_ocorrencia + indexacao