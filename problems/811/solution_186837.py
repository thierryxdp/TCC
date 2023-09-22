def colchao(medidas,H,L):
    """Retorna uma função que diz se um colchão de medidas A, B e C(que devem estar
dentro de uma lista com o nome "medidas") passa por uma porta de altura H e largura L;
Entrada-> Lista e int, Saida-> Lista e int->boleano"""
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    
    if H>=A and L>=B:
        return True
    if H>=B and L>=A:
        return True
    else:
        return False