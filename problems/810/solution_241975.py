def retira_pontuacao(frase):
    '''dada uma frase(frase), retorna uma string correspondente a frase, com todas as pontuacoes substituidas por espaco; str -> str'''
    A = str.replace(frase, '-',' ')
    B = str.replace(A, ',',' ')
    C = str.replace(B, ':',' ')
    D = str.replace(C, ';',' ')
    E = str.replace(D, '.',' ')
    F = str.replace(E, '!',' ')
    G = str.replace(F, '?',' ')
    return G
def inverte(frase):
    '''dada uma frase(frase), retorna a mesma na ordem inversa, sem letras maiusculas e sem a pontuacao; str -> str'''
    A = retira_pontuacao(frase)
    B = str.split(A)
    C = list.reverse(B)
    D = (B)
    E = str.join(' ',D)
    return E