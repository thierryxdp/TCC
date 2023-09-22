def posLetra(string,letra,ocorrencia):
    """Função que, dada uma string, uma letra e um número que indica a ocorrência desejada da letra, retorna a posição da string onde está a ocorrência daquela letra. Se tiverem menos ocorrências da letra do que a ocorrência pedida, vai retornar -1. str, str, int-> int""" 
    string = list(string)
    ocorrencias = []
    s = 0 
    while s < len(string):
        if string[s] == letra:
            ocorrencias.append(s)
            s += 1
    if ocorrencia <= (len(ocorrencias)):
        ocorrencia = ocorrencia-1
        ocorrencias[ocorrencia]
        return ocorrencias[ocorrencia]
    else:
        return -1