def posLetra(string, letra, ocorrencia):
    '''dadas uma string, uma letra e a sua ocorrencia, retorna em que posiçao da string aquela ocorrencia está.
       caso exista menos ocorrencias do que a pedida, a função deve retornar -1
       : str, str, int -> int
    '''
    x = string.find(letra)
    i = x+1
    qtd
    while i < len(string):
        qtd = qtd + string.replace(x, '.') 
        i = i + 1
    return qtd