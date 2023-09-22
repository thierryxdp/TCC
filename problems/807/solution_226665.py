def conta_frases(texto):
    '''Função que retorna quantas frases há em um texto, dado o texto a ser
    analisado.
    texto -> string
    return -> int'''
    
    texto = texto.strip()
    unificacao = texto.replace('!', '.').replace('?', '.').replace('...', '.')
    
    unificacao = unificacao.split('.')
    unificacao = unificacao.remove(len(unificacao))
    
    return len(unificacao)