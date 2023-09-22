# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,h,l):
    [a,b,c] = medidas
    menor = min(a, min(b,c))
    segunda_menor = min(max(medidas[0],medidas[1])), min(max(medidas[0],medidas[2])), max(medidas[1],medidas[2])	
    
    if (menor <= l) and (segunda_menor <= h):
        return True
    else:
        return False