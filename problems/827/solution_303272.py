def qtd_divisores(n):
    """conta quantos divisores um dado número inteiro tem
Exemplo:
>>>qtd_divisores(10) --  1, 2, 5 e 10; total de 4 divisores"""
    divisores = [] #criando uma lista
    i = 0
    nova = list(range(1,n+1)) #a partir do numero para não dar esse no proximo passo
    
    while i < len(list(range(n))):
        if n%nova[i] == 0: #caso comece no zero, dará erro
            divisores += [i+1] #soma 1 para realocar no numero de divisao correto
            
        i += 1
        
    return len(divisores) #quantidade de divisores