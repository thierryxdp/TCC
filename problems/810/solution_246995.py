def retira_pontuacao(frase):
    '''Função que substitui todas as pontuações de uma frase por espaçamentos.
    frase -> string
    return -> string'''
    
    
    frase = frase.replace('-', '').replace(',', '').replace(':', '').replace(';','')
    frase = frase.rstrip('.').rstrip('?').rstrip('!')
    
    return frase






def inverte(frase):
    '''Função que retorna a frase no sentido inverso, sem pontuação e sem
    letra maiúscula, dada a frase a ser modificada.
    frase -> string
    return -> string'''
    
    dado_pronto = retira_pontuacao(frase).lower().split(' ')
    
    
    
    inverso = dado_pronto[-1: -(len(dado_pronto)+1): -1]
    inverso = str.join(' ', inverso)
    return inverso