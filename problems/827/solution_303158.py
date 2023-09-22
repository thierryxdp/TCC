def divisores(x):
    """Função que recebe x como entrada e calcula quantos divisores ele tem.
        int -> int"""
    lista=[]
    for i in range(1,x+1):
        if x%i==0:
            lista=lista+[i]
    return len(lista)