def colchao(medidas,H,L):
    """Esta é a função que dada uma lista com as três medidas de um colchão(ordenadas de menor para maior) e a altura e largura de uma porta retorna se o colchão passará pela porta ou não: list, int, int -> str"""
    #Medidas= A(largura), B(comprimento), C(altura)#
    A= medidas[0]
    B= medidas[1]
    C= medidas[2]
    if C <= H and B <= L or B <= H and A <= L :
        return "True"
    else:
        return "False"