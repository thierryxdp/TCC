# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Retorna uma lista intercalada entre as duas listas que foram dadas
    Lista,Lista -> Lista """
    lista = []
    for i in range (len(lista1)):
        lista.append(lista1[i])
        lista.append(lista2[i])
    return lista