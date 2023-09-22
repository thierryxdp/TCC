def primo(numero):
    '''Função que dado um número inteiro positivo como entrada, 
    verifica se este número é primo ou não;
    int -> booleano'''
    
    lista = []
    A = range(numero+1)
    for num in A[1:] :
        if numero % num == 0:
           lista = lista + [numero]
           
    if len(lista) == 2:
        return True
    else:
        return False