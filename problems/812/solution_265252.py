def retira_pontuacao(frase):
    '''Funcao que dada uma frase retorna a mesma frase onde
    todos os caracteres de pontuacao foram substituidos por
    espaco.
    Parametro:
    Str
    Saida:Str'''
    
    h= str.replace(frase,'.',' ')
    i= str.replace(h,'!',' ')
    j= str.replace(i,'...',' ')
    k= str.replace(j,'?',' ')
    l= str.replace(k,',',' ')
    m= str.replace(l,'-',' ')
    n= str.replace(m,':',' ')
    o= str.replace(n,';',' ')
    
    return o