# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """define se um colchão passa por uma porta;list,int,int->bool"""
    portas=[H+L]
    medidas2= [medidas[1]+medidas[2]] 
    altura=[H]
    largura=[L]
    largura_colchao=[medidas[1]]
    comprimento_colchao=[medidas[2]]
    if medidas2>portas:
        return medidas2>portas
    else:
        if largura_colchao<altura or comprimento_colchao<largura:
            return largura_colchao<altura