def retira_pontuacao(frase):
    """Dada uma frase a função retorna outra frase onde todos os caracteres como pontos,
    vírgula, travessão, ponto e vírgula, dois pontos e a pontuação de encerramento da
    frase são substituídos por espaço;
    str --> str"""
    A = str.replace(frase,'...',' ')
    B = str.replace(A,'!',' ')
    C = str.replace(B,'?',' ')
    D = str.replace(C,',',' ')
    E = str.replace(D,'-',' ')
    F = str.replace(E,':',' ')
    G = str.replace(F,'.',' ')
    H = str.replace(G,';',' ')
    return H