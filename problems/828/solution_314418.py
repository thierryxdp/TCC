def primo(numero):
    ''' Função que dado um número inteiro positivo, retorna
    True se ele for primo e False, caso contrário.
    Entrada: int
    Retorno: bool '''
    
    numeros_primos = [2]
    for x in range(3,numero,2):
        if (numero%x)!= 0:
            list.append(numeros_primos,x)
    return numero in numeros_primos