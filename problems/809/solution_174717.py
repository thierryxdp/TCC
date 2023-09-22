# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que retorna uma lista formada pelos elementos da primeira e da segunda
    lista intercalados.
    lista, lista -> lista"""
    
  
    
    lista_nova = lista1[0:1] + lista2[0:1] + 
    lista1[1:2] + lista2[1:2] + lista1[:2] + 
    lista2[:2]
    
    return lista_nova