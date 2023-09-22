ef retira_pontuacao (frase):
    '''função em que dada uma frase retorne a frase onde todos os caracteres da pontuação tenham sido substituídos por espaços;
    str -> str'''
    A=(str.replace(frase,'!',' '))
    B=(str.replace(A,'?',' '))
    C=(str.replace(B,'...',' '))
    D=(str.replace(C,'.',' '))
    E=(str.replace(D,',',' '))
    F=(str.replace(E,';',' '))
    G=(str.replace(F,':',' '))
    H=(str.replace(G,'-',' '))
    return H