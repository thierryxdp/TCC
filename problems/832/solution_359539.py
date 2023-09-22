def eh_quadrada(A):
    """Dada uma função retorna um valor booleano que informa se ela é uma matriz quadrada ou não (ou seja o número de colunas é igual ao de linhas.list(list)->bool."""
    numero=len(A)
    lista=[]
    if A==[]:
        return True
    for elem in range(numero):
        numero2=len(A[elem])
        list.append(lista,numero2)
    if sum(lista)==(len(A[0])*len(A)):
        return True
    else:
        return False