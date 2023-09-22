# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Retorna uma lista intercalada de maneira crescente dado duas
     listas
     assinatura: lista,lista --> lista
     teste: 
     intercala([1,3,5],[2,4,6])==[1,2,3,4,5,6]"""
    lista3 = [lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]]
    return lista3