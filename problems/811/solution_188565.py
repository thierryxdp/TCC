# Função que retorna true se o colchão passar pela porta e false se não passar
# medidas, que são largura, compomprimento e altura do colchão,H,L, altura e largura da porta de casa
# lista;float;float->bol
def colchao(medidas,H,L):
    medidas=[a,b,c]
    if a<=H and b<=L or a<=H and c<=L or a<=L and b<=H or a<=L and c<=H:
        return "true"