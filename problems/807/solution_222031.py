def conta_frases(texto):
    ''' Função que conta quantas frases
        aparecem em um dado texto.
        str -> int '''
    
    pontos, exclama, pergunta, reticencias = 1, 1, 1, 1 
    
    if texto.find('.') == -1:
        pontos = 0 
        reticencias = 0
    
    if texto.find('!') == -1:
        exclama = 0
    
    if texto.find('?') == -1:
        pergunta = 0
    
    if texto.find('...') == -1:
        reticencias = 0
     
    return pontos + exclama + pergunta + reticencias