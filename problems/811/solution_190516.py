# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    '''funcao que retorna se o colchão passa pela porta.
    lista,int,int->boolean'''
    altura_c=medidas[2]
    largura_c=medidas[1]
    prof_c=medidas[0]
    
    if largura_c<=H:
        return True
    elif altura_c>H and largura_c>L:
        return False
    else:
        return True