def posLetra(string,letra,n_ocorrencia):
    '''função que dado uma string, uma letra e o numero de ocorrecias da letra,
    retorna a posição da ocorencia desejada da letra, caso exista menos ocorrencias
    da letra que a ocorrencia dada retorna -1
    str, str, int-> int'''
    if str.count(string,letra)<n_ocorrencia:
        return -1
    else:
        return (n_ocorrencia*str.count(string,letra))/n_ocorrencia