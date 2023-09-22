# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    l1=lista1
    l2=lista2
    s=(l1[0],l1[1],l1[2],l2[0],l2[1],l2[2])
    
    a=min(s)
    s=list.remove(s,a)
    
    b=min(s)
    s=list.remove(s,b)
    
    c=min(s)
    s=list.remove(s,c)
    
    d=min(s)
    s=list.remove(s,d)
    
    e=min(s)
    s=list.remove(s,e)
    
    f=min(s)
    s=list.remove(s,f)
    
    return a,b,c,d,e,f