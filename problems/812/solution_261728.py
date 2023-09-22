def retira_pontuacao(s):
    """Função que dada uma frase, retorna uma frase onde todos os caracteres de pontuação tenham sido substitúidos por espaçoes."""
    A = str.replace(str(s),':',' ')
    B = str.replace(str(A),';',' ')
    C = str.replace(str(B),'.',' ')
    D = str.replace(str(C),',',' ')
    E = str.replace(str(D),'—',' ')
    F = str.replace(str(E),'-',' ')
    G = str.replace(str(F),'!',' ')
    H = str.replace(str(G),'?',' ')
    return H