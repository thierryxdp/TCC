def posLetra(string,letra,numero):
    '''retorna a posição em que a letra encontra-se na string na ocorrência
    indicada pelo número e, caso o número de ocorrências da letra seja menor 
    que o número da ocorrência desejada, retorna -1;
    str, str, int -> int'''
    
    quant_ocorrencias = str.count(string,letra)
    
    if quant_ocorrencias < numero:
        return -1
    else:
        x = str.replace(string,letra,' ',numero-1)
        posicao = str.index(x,letra)
        return posicao