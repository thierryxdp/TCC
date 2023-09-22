def retira_pontuacao(frase):
    
    A = str.join(' ', str.split(frase, '.'))
    B = str.join(' ', str.split(A, ','))
    C = str.join(' ', str.split(B, '?'))
    C = str.join(' ', str.split(C, '!'))
    E = str.join(' ', str.split(D, '-'))
    return E