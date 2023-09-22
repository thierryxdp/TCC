# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(l1, l2):
    """Dadas duas listas (l1),(l2),ambas com 3 elementos,
    intercala elas.
    list,list --> list"""
    l=[]
    a,b,c=l1
    d,e,f=l2
    lista= [a,]+[d,]+[b,]+[e,]+[c,]+[f,]
    return l+lista