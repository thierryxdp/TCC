def quant_palavras(frase):
    
    '''
    funcao que dada uma frase, retorna o numero de palavras da frase. Para isso, 
    utiliza a função split, em todas as pontuações e faz a contagem por ela e pelo espaço
    :frases--->str
    :return---> int
    '''
    ponto_final = frases.replace("...", '@')
    ponto_exclamacao = ponto_final.replace("!", '@')
    ponto_interrogacao = ponto_exclamacao.replace("?", '@')
    reticencias = ponto_interrogacao.replace(".", '@')
    
    
    return reticencias.count('@')