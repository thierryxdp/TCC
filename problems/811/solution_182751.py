# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''
    dado as medidas do colchao entre parenteses (do menor para o maior),
    as medida da porta altura H e largura L, retorna True se o colchao passar na porta e
    False se for o contrário.
    entrada:(int,int,int),int,int
    saida:bool
    '''
    medidas=medidas[0],medidas[1],medidas[2]
    return medidas[1]<=H