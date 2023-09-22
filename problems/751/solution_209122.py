def quant_palavras(frase):
    '''Função que, dado o parâmetro de entrada frase(i),utiliza a função split para retornar uma lista com as palavras separadas e a função len para verificar o tamanho da nova lista formada (t) e desta maneira retorna a quantidade de palavras na frase
dada. string> int'''
    i= frase
    t=str.split(i)
    x= len(t)
    
    return x