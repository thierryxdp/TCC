def faltante(n):
    """Função que dada uma lista n -1 descubra qual a peça que está faltando; int-> int"""
    i=0
    s=[]
    while n[i]<len(n):
        if s==s+1:
            i=i+1
    return s