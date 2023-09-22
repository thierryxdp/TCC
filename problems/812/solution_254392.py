def retira_pontuacao(s):
    '''
    Esta função recebe um texto e retorna uma string contendo o texto fornecido
    tendo substituido toda pontuação com espaços.
    
    Parametros
    ----------
   	s (str) : texto
    '''
    l = [',', '.', ';', ':', '-', '!', '?']
    for i in range(len(s)):
        if s[i] in l:
            s = s.replace(s[i], ' ')
    return s