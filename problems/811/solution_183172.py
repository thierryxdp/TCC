def colchao(medidas, H, L):
    """Recebe 3 parametros: medidas (list), H (int), L (int) em centimetro.
        Primeiramente, obtemos as medidas do colchao, comprimento para a maior,
        largura para a segunda maior medida, e altura para a menor medida.
        Por fim, verifica-se as condicoes de tamanho estao estabelecidas.
        Obs: considerar que a altura do colchao seja de acordo com a realidade"""
        
    comprimentoColchao = max(medidas)
    alturaColchao = min(medidas)
    larguraColchao = (medidas[0] + medidas[1] + medidas[2]) - (max(medidas) + min(medidas))

    if H >= comprimentoColchao or H >= larguraColchao or L >= comprimentoColchao or L >= larguraColchao:
        return True
    return False