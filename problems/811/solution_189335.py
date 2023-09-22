# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(lista,h,l):
    if lista[1] <= h or lista[2] < h:
        return True
    if lista[1] >h or lista[2] > h:
        return False