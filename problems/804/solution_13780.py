def filtra_pares(A):
#filtragem
    """Função que, ao receber uma tupla A contendo quatro inteiros, retorna uma 
    segunda tupla contendo os termos pares de A.
       tupla (int, int, int, int) -> tupla"""
    t = ()
    if A[0]%2 == 0:
        t = t + (A[0],)
    if A[1]%2 == 0:
        t = t + (A[1],)
    if A[2]%2 == 0:
        t = t + (A[2],)
    if A[3]%2 == 0:
        t = t + (A[3],)
    return t
 
    #Teste 1:
    #filtra_pares((1,2,3,4))--> (2,4)
    
    #Teste 2:
    #filtra_pares((2,4,6,8))--> (2,4,6,8)
    
    #Teste 3:
    #filtra_pares((1,3,5,7))--> ()