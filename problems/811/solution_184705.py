#------EXERCICIO 7------

def colchao(medidas,H,L):
    '''Verifica se colchao(axBxC) passa pela porta(LxH)
          Obs.: ASSUME as dimensões do colchão
             ordenadas em ordem crescente
       [float,float,float],float,float -> bool'''

    lado1 = medidas[0]
    lado2 = medidas[1]
    lado3 = medidas[2]

    if (lado1<=H and lado2<=L) or (lado2<=H and lado3<=L) or (lado3<=H and lado1<=L) or (lado2<=H and lado1<=L) or (lado3<=H and lado2<=L) or (lado1<=H and lado3<=L):
        return True
    else:
        return False