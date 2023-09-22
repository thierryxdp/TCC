def posLetra(frase, letra, ocorrencia):
    '''função que recebe como entrada uma string, uma letra e um número
    que indica a ocorrencia desejada da letra (1 para primeira, 2 para a
    segunda, etc) e retorna em que posição da string aquela ocorrencia da
    letra está. Caso exista menos ocorrências da letra do que a ocorrencia
    pedida, a função deve retornar -1.
    str, str, int -> int''' 
   
    i = 0
    posicaoletra = 0
    posicaooutrasletras = 0
    
    
    while i<len(frase): 
        if frase[i] is letra:
            posicao += 1
        i += 1
        if frase[i] is not letra:
            posicaooutrasletras += 1
        i += 1
            
        if ocorrencia > frase.count(letra):
            return -1
    return posicaooutrasletras + posicaoletra