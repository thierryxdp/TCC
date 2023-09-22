# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    #intercala duas listas e retorna na forma de uma nova lista
    lista3 = []
    i = 0
    while i < len(lista1):
		lista3+= lista1[i] + lista2[i]
        i++
    return lista3