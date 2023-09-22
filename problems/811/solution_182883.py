# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas, H, L):
    '''Dadas uma lista medidas com as medidas de um colchâo
    retorna se o colchão passa ou não por uma porta de 
    dimensões H, L
    list, int, int -> bool'''
    porta = (H,L)
    return medidas[0] <= min(porta) and medidas[1] <= max(porta)