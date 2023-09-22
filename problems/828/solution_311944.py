def primo(num): 
    """Função que dado um numero inteiro e positivo, retorne se é positivo ou não; int->bool""" 
    lista = [] 
    i = 1 
    while i < num + 1: 
        if num % i == 0:
            list.append(lista,i)
        i = i + 1 
    if len(lista) == 2: 
        return True
    else:
        return False