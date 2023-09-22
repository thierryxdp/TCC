# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que dadas duas listas de tamanhon 3, gera uma outra lista L3, intercalando os elementos das duas listas inseridas"
    list, list -> list
    
    Parameters:
   lista1: Parâmetro do tipo lista que representa a primeira lista inserida
   lista2: Parâmetro do tipo lista que representa a segunda lista inserida
    
    """
    intercala = []
    for a, b in zip(lista1,lista2):
        intercala.append(a)
        intercala.append(b)
    return intercala