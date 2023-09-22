# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """Retorna se Joao consegue ou nao passar o colchao pela
    porta de sua casa dadas: medidas em lista do colchao 
    (exemplo "[25,120,220]"), L(largura da porta) e H(altura da
    porta). A Resposta True=quando conseguir passar e False=quando
    nao"""
    
    if medidas[1]<=H and medidas[0]<=L:
        return True
    else:
        return False