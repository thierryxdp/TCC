# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Recebe duas listas (lista1, lista2) e gera uma terceira
    lista que intercala os elementos da lista original."""
    return [lista1[0]] + [lista2[0]] + [lista1[1]] + [lista2[1]] + [lista1[2]] + [lista2[2]] + [lista2[2]]