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