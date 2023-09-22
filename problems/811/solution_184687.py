# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """define se um colchão passa por uma porta;list,int,int->bool""" 
    altura=[H]
    largura=[L]
    largura_colchao=[medidas[1]]
    comprimento_colchao=[medidas[2]]
    if largura_colchao>altura and comprimento_colchao>largura:
        return 2==3
    else:
        if largura_colchao<altura and comprimento_colchao<largura:
            return 2==2
        else:
            if largura_colchao>altura or comprimento_colchao<largura:
                return 2==2
            else:
                largura_colchao<altura and comprimento_colchao>largura:
                    return 2==2