def colchao(medidas,H,L):
    """funcao que calcula se um colchao novo comprado consegue passar pela porta da casa,
    a primeira entrada e uma lista com 3 tamanhos inteiros, e H, L sao respectivamente
    a altura e a largura da porta, importante salientar que o colchao pode ser virado para
    passar na porta, ou seja, pode passar deitado ou de lado;
    list, int, int -> bool"""
    #passando deitado
    if L >= medidas[1] and H >= medidas[0]:
        return True
    #passando de lado
    if medidas[0] <= L and medidas[1] <= H:
        return True
    else:
        return False