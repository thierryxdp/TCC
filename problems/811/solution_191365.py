def colchao(lista1, H, L):
    """Recebe uma lista de 3 elementos com
as dimensões do colchão (da menor para a maior) e
dois inteiros que representam a altura >H< e a largura >L<
da porta, respectivamente. Retorna True se o colchão
passar pelas portas ou False se não.
assinatura: list, int, int --> bool
casos de testes:
colchao([25,120,220], 200, 100) == True
colchao([25,205,220], 200, 100) == False
colchao([25,200,220], 200, 100) == True
colchao([36,190,209], 187, 248) == True
"""
    if lista1[0] <= L and lista1[1] <= H:
        return True
    elif lista1[1] <= L and lista1[0] <= H:
        return True
    else:
        return False