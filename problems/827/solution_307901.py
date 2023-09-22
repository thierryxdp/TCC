def qtd_divisores(num):
    """
    Função que calcula quantos divisores um número possui.
    int -> int
    """
    
    soma = 0
    numeros_possiveis = list(range(1,num+1))
    i = 0
    
    for elemento in numeros_possiveis:
        if (num%numeros_possiveis[i] == 0):
            soma = soma + 1
            
        i = i + 1
    return soma