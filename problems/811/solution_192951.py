# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(dimensoes_colchao,H,L):
    """Função que define se o colchão passa ou não  pelas portas 
    int -> string"""
    if dimensoes_colchao[1] <= H or dimensoes_colchao[2] <= L:
        return True
    else:
        return False