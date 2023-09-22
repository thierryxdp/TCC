'''funcao que retorna se colchao passa pela porta de acordo com medidas'''
def colchao(medidas,altura_porta,largura_porta):
    list.sort(medidas)
    menor_colchao = medidas[0]
    maior_colchao = medidas[1]
    menor_porta = min(altura_porta,largura_porta)
    maior_porta = max(altura_porta,largura_porta)
    
    if menor_colchao > menor_porta or maior_colchao > maior_porta:
        return False
    # else implícito
    return True