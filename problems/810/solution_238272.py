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
def inverte(f):
    '''Dada uma frae f,retorna uma outra frase que contenha as mesmas 
    palavras da frase de entrada na ordem inversa, sem letras maiusculas,
    e sem a pontuacao.
    str->str'''
    
    sem_pont=retira_pontuacao(f)
    sem_mai=str.lower(sem_pont)
    lista=str.split(sem_mai)
    lista_inv=lista[::-1]
    
    return lista