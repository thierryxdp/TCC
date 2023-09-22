posLetra(string,letra,n):
    """ retorna em que posicao da string uma ocorrencia
    da letra esta, dados uma string, uma letra e um 
    numero n referente a ocorrencia desejada da letra
    caso exista menos ocorrencias da letra do que a   
    ocorrencia pedida a funcao retorna o int -1
    str, str, int -> int"""
    busca = string.find(letra)
    while busca >= 0 and n > 1:
        busca = string.find(letra, busca + 1)
        n -= 1
    return busca