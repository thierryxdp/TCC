# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que retorna uma lista formada pelos elementos da primeira e da segunda
    lista intercalados.
    lista, lista -> lista"""
    
    elementos_lista1 = lista1.split(" ")
    elementos_lista2 = lista2.split(" ")
    
    lista_nova = elementos_lista1[0:1] + elementos_lista2[0:1] + 
    elementos_lista1[1:2] + elementos_lista2[1:2] + elementos_lista1[:2] + 
    elementos_lista2[:2]
    
    return lista_nova