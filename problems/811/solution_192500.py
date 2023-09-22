# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variávei
def colchao(medidas, h, l):
    list.sort(medidas)
    menor_colchao = medidas[0]
    maior_colchao = medidas[1]
    menor_porta = min(altura_porta,largura_porta)
    maior_porta = max(altura_porta,largura_porta)
    
    if menor_colchao > menor_porta or maior_colchao > maior_porta:
        return False
    # else implícito
    return True