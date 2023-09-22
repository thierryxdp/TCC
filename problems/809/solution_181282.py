# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Recebe duas listas como parametro e retorna uma lista
    que contem todos os valores intercalados entre si;
    lista<???>[3], lista<???>[3] > --> lista[6]"""
    
    buffer_lista = []

    buffer_lista += [lista1[0], lista2[0],]
    buffer_lista += [lista1[1], lista2[1],]
    buffer_lista += [lista1[2], lista2[2],]
    
    returun buffer_lista