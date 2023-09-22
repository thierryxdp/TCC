# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Retorna uma lista intercalada com elementos de duas
       listas dadas de tamanho 3;
       list, list -> list"""
    
    lista = []
    
    for n in range(3):
        
        lista.append(lista1[n])
        lista2.append(lista2[n])
        
    return lista