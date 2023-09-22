# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    list.sort(medidas)
    lista1 = [H,L]
    list.sort(lista1)
    if (medidas[0] < lista1[0]) and (medidas[1] < lista1[1]):
        return True
    else:
        return False