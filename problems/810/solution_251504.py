def inverte2(frase):
    '''dada uma frase(frase), retorna a mesma na ordem inversa, sem letras maiusculas e sem a pontuacao; str -> str'''
    A = retira_pontuacao(frase)
    B = str.split(A)
    C = list.reverse(B)
    D = (B)
    E = str.join(' ',D)
    return E