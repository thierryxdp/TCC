def qtd_divisores(num):
    '''
    	Função que conta quantos divisores um número tem.
        int -> int
    '''
    lista_de_divisores = []
    tamanho = (num//2)+1
    
    if num % num == 0: #Verifica se é divisível por ele mesmo
        lista_de_divisores.append(num)
        
    for possivel_divisor in range(1, tamanho):
        if num % possivel_divisor == 0:
            lista_de_divisores.append(possivel_divisor)
    if num==0:
        return 0
    return len(lista_de_divisores)