# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """returna True se o colchao passa pela porta e False caso o colchao não passe pela porta.
    Parametros:
    Entrada:list,int,int
    Saída:Booleano"""
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    return ((A and B) or (A and C) or (C and N))<=(H or L)