def hashtag(s):
    '''
    edita a função de entrada tal que ela passe a 
    carregar um sinal de # em seu início, em seu meio
    e em seu fim
    '''
    indice_meio = int(len(s))/2
    parte1 = s[:indice_meio]
    parte2 = s[1+indice_meio:]
    S = '#' + parte1 + '#' + parte2 + '#'
    return S