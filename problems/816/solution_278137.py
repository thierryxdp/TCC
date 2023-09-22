def maiores(a,b):
    """list,int->list
    retorna uma lista com todos os inteiros em a menos que b"""
    i=0
    c=[]
    while a[i]<b:
        c=c+a[i]
        i=i+1
    return c