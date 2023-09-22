# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que recebe 2 lista intercalando-as 
list,list = list"""
    X = list(lista1)
    Y = list(lista2)
    x0 = list(X[:1])
    x1 = list(X[1:2])
    x2 = list(X[2:])
    y0 = list(Y[:1])
    y1 = list(Y[1:2])
    y2 = list(Y[2:])
    
    z = x0 + y0 + x1 + y1 + x2 + y2
    return list(z)