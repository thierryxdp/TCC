# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,altura_porta,largura_porta):
    '''Função que define por colchão as medidas, altura e largura da porta 
       e returne True se o colchão passa pelas portas e False caso contrário.
       list --> bool'''
    list.sort(medidas)
    menor_colchao = medidas[0]
    maior_colchao = medidas[1]
    menor_porta = min(altura_porta,largura_porta)
    maior_porta = max(altura_porta,largura_porta)
    
    if menor_colchao > menor_porta or maior_colchao > maior_porta:
        return False
    else:
        return True