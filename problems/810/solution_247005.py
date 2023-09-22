def retira_pontuacao(frase):
    '''Função que substitui todas as pontuações de uma frase por espaçamentos.
    frase -> string
    return -> string'''
    
    
    frase = frase.replace('-', ' ').replace(',', '').replace(':', '').replace(';','')
    frase = frase.rstrip('.').rstrip('?').rstrip('!')
    
    return frase









def inverte(frase):
    '''função que dada uma frase, retorna essa mesma frase ao inverso.
    frase -> str
    return -> str'''
    
    semPontuacao = retira_pontuacao(frase).lower().split(' ')
    
    semPontuacao.sort(reverse = True)
    
    semPontuacao = str.join(' ', semPontuacao)
    
    return semPontuacao