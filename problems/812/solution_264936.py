def retira_pontuacao(frase):
    '''
    Funçao que dada uma frase, a retorna com todos os caracteres de
    pontuaçao substituidos por espaço
    str -> str
    '''
    trav=str.replace(frase,'-',' ')
    virg=str.replace(trav,',',' ')
    dois=str.replace(virg,':',' ')
    p_vir=str.replace(dois,';',' ')
    final=str.replace(p_vir,'.',' ')
    excla=str.replace(final,'!',' ')
    inter=str.replace(excla,'?',' ')
    
    return inter