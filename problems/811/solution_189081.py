# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    ordenado = list.sort(medidas)
    lista1 = [H,L]
    ordenado2 = list.sort(lista1)
    if (ordenado[0] < ordenado2[0]) and (ordenado[1] < ordenado2[1]):
        return True
    else:
        return False