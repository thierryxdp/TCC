def posLetra(palavra,letra,num_ocorrencia):
    """ Funcao que retorna a posicao da string a ocorrencia da letra . Str, chr , int-->Int"""
     count = 0
    soma = 0
    if str.count(palavra,letra) < num_ocorrencia:
        return -1
    else:
        while count < num_ocorrencia:
            soma += str.index(palavra,letra,count)
            count += 1
        return str.index(palavra,letra,soma)