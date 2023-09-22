def colchao(li, h, l):
    """Função que recebe como parâmetros de entrada uma lista li com as dimensões A, B e C de um colchão em centímetros,
ordenadas da menor para a maior, e dois inteiros h e l, correspondentes respectivamente a altura e a
largura das portas em centímetros, e retorna se o colchão passa pelas portas ou não, com True ou False.
list, int, int -> bool"""
    

    if li[0]<=l and li[1]<=h:
        return True
    
    elif li[0]<=h and li[1]<=l:
        return True
    
    elif li[0]<=l and li[2]<=h:
        return True

    elif li[1]<=l and li[2]<=h:
        return True
    else:
        return False