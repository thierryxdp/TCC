def qtd_divisores(numero):
    """dado um número inteiro, a função conta quantos divisores esse número tem  (int->int)"""
    if numero == 0 :  
        return "O número zero tem infinitos divisores"  #cas o número inserido seja zero, retorna uma mensagem, uma vez que não existe um número definido de divisores para zero
    Num_de_div = 0 #cria-se o acumulador
    lista_dos_poss_div = list(range(1,numero+1)) #cria-se uma lista que vai de 1 até o número inserido, ou seja, uma lista com todos os possiveis divisores
    for numero_i in lista_dos_poss_div : 
        if numero % numero_i == 0 :  
            Num_de_div = Num_de_div + 1  
    return Num_de_div