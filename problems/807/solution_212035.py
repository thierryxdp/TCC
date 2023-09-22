def conta_frases (texto):
    '''função que retorna o número de frases em um texto. Uma frase é contabilizada em todo ponto final, exclamação
    interrogação ou reticências.
    string -> int'''
    reticencias = str.replace(texto, '...', 'fim da frase')
    interrogacao = str.replace(reticencias, '?', 'fim da frase')
    exclamacao = str.replace(interrogacao, '!', 'fim da frase')
    ponto = str.replace(exclamacao, '.', 'fim da frase')
    return (len(str.split(ponto, 'fim da frase')) - 1)
### a presença do -1 se dá pois um dos pontos será o fim do texto, e o python irá retornar uma lista com uma string vazia no final