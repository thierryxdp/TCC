def qtd_divisores(num):
    '''
    	Função que conta quantos divisores um número tem.
        int -> int
    '''
    lista_de_divisores = []
    tamanho = (num//2)
    return tamanho
    for possivel_divisor in range(1, tamanho):
        if num % possivel_divisor == 0:
            lista_de_divisores.append(possivel_divisor)
    return len(lista_de_divisores)