def colchao(medidas,H,L):
    ''' Função que dados uma lista (medidas) que representa as dimensões de um
    colchão do menor para o maior valor, em cm, e as medidas da altura (H) e
    largura (L) de uma porta, em cm, retorna True se o colchão passa pela porta
    e, False, caso contrário.
    Entrada: list, int, int
    Retorno: bool '''

    medida_A = medidas[0]
    medida_B = medidas[1]
    medida_C = medidas[2]

    if ((medida_A <= L and medida_B <= H) or (medida_A <= L and medida_C <= H) or
        (medida_B <=L and medida_C <= H)):
            return True

    elif ((medida_A <= H and medida_B <= L) or (medida_A <= H and medida_C <= L) or
          (medida_B <= H and medida_C <= L)):
            return True
    

    else:
        return False