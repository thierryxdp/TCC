# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """define se um colchão passa por uma porta;list,int,int->bool"""
    portas=[H+L]
    medidas2= [medidas[1]+medidas[2]] 
    if medidas2>portas:
        return false