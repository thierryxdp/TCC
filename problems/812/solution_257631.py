def retira_pontuacao(frase):
    '''Dada uma frase, retorna essa mesma frase com os caracteres de 
    pontuacao substituidos por espaço
    str->str'''
    
    f=frase
    trav=str.replace(f,'-',' ')
    vir=str.replace(trav,',',' ')
    doisp=str.replace(vir,':',' ')
    pvir=str.replace(doisp,';',' ')
    pf=str.replace(pvir,'.',' ')
    exc=str.replace(pf,'!',' ')
    inter=str.replace(exc,'?',' ')
    
    return inter