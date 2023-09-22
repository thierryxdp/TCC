# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    "Função para saber se consegue passar o colchão pelas portas. list,float,float->bool"
    list.sort(medidas)
    menor_colchao = medidas[0]
    maior_colchao = medidas[1]
    menor_porta = min(H,L)
    maior_porta = max(H,L)
    
    if menor_colchao > menor_porta or maior_colchao > maior_porta:
        return False
    else:
        return True