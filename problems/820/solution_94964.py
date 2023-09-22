def posLetra(string, letra, numero):
    '''Função que retorna em que posição da string a
    ocorrência desejada da letra está.
    Dados de entrada: str, str, int
    Valor de saída: int
    '''
    ocorrencias = str.count(string,letra)
    if ocorrencias < numero:
        return -1 
    else:
        x = str.replace(string, letra, ' ', numero-1)
        posicao = str.index(x, letra)
        return posicao