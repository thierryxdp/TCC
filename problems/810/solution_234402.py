def retira_pontuacao(s):
    '''
    Esta função recebe um texto e retorna uma string contendo uma cópia do texto fornecido
    sem pontuação.
    
    Parametros
    ----------
    s (str) : texto
    '''
    l = [',', '.', '!', ';', ':', '?', '-']
    for i in range(len(s)):
        if s[i] in l:
            s = s.replace(s[i], ' ')
    return s

def inverte(s):
    '''
    Esta função recebe um texto e retorna uma string contendo uma cópia do texto fornecido, sem letras
    maiúsculas, sem pontuação e com a ordem das palavras invertida.
    
    Parametros
    ----------
    s (str) : texto
    '''
    s0 = retira_pontuacao(s).lower().split()[::-1]
    s = ' '.join(s0)
    return s