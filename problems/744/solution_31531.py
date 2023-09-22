def hashtag(s):
    '''
    edita a função de entrada tal que ela passe a 
    carregar um sinal de # em seu início, em seu meio
    e em seu fim
    '''
    i = int(len(s)/2)
    parte1 = s[:i]
    parte2 = s[1+i:]
    S = '#' + parte1 + '#' + parte2 + '#'
    return S