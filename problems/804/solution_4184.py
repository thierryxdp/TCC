#Start your python function here
def filtra_pares(inteiros):
    """funcao que recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla,
    contendo apenas os elementos pares da tupla. tuple->tuple"""
    inteiros=[n1,n2,n3,n4]
    n1=inteiros[0]
    n2=inteiros[1]
    n3=inteiros[2]
    n4=inteiros[3]
    if n1%2==0 and not (n2%2==0 and n3%2==0 and n4%2==0):
        return (n1)
    elif n2%2==0 and not (n1%2==0 and n3%2==0 and n4%2==0):
        return (n2)
    elif n4%2==0 and not (n2%2==0 and n3%2==0 and n1%2==0):
        return (n4)
    elif n3%2==0 and not (n2%2==0 and n1%2==0 and n4%2==0):
        return (n3)
    elif n1%2==0 and n2%2==0 and not (n3%2==0 and n4%2==0):
        return (n1,n2)
    elif n1%2==0 and n3%2==0 and not (n2%2==0 and n4%2==0):
        return (n1,n3)
    elif n1%2==0 and n4%2==0 and not (n3%2==0 and n2%2==0):
        return (n1,n4)
    elif n2%2==0 and n3%2==0 and not (n1%2==0 and n4%2==0):
        return (n2,n3)
    elif n2%2==0 and n4%2==0 and not (n3%2==0 and n1%2==0):
        return (n2,n4)
    elif n3%2==0 and n4%2==0 and not (n1%2==0 and n2%2==0):
        return (n3,n4)
    elif n1%2==0 and n2%2==0 and n3%2==0 and not (n4%2==0):
        return (n1,n2,n3)
    elif n1%2==0 and n2%2==0 and n4%2==0 and not (n4%2==0):
        return (n1,n2,n4)
    elif n1%2==0 and n4%2==0 and n3%2==0 and not (n2%2==0):
        return (n1,n3,n4)
    elif n4%2==0 and n2%2==0 and n3%2==0 and not (n1%2==0):
        return (n2,n3,n4)
    elif n1%2==0 and n2%2==0 and n3%2==0 and n4%2==0:
        return (n1,n2,n3,n4)
    else:
        return ()