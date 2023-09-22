def colchao(C, H, L):
    """Função que define se o colchão passa ou não pela porta da casa de João.
       lista, int, int -> bool
       Explicação: A função acima recebe uma lista com as dimensões do colchão
       (altura, largura e comprimento) ordenados do menor para o maior,
       além das dimensões da porta (altura e largura).
       Ao interpretar os dados de entrada, retorna 'True' caso o colchão 
       passe pela porta e 'False' caso contrário. Basicamente, para retornar
       'True' apenas um valor da lista pode ser maior que o maior dos inteiros
       de fora."""
    A = C[0]
    B = C[1]
    C = C[2]

    if (H > L and (A > H or B > H)) or (L > H and (A > L or B > L)):
        return False
    else:
        return True

#Teste 1:
#colchao([25, 120, 220], 200, 100)--> True

#Teste 2:
#colchao([25, 205, 220], 200, 100)--> False

#Teste 3:
#colchao([25, 200, 220], 200, 100)--> True