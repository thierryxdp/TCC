# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """ Funcao que retorna um lista que ér formada pela intercalacao de duas listas;
    	list, list -> list
    """
    lista3 = lista1 + lista2
    lista3.sort()
    
    elemento_anterior = lista3[0]
    lista3_sem_duplicadas = [lista[0]]
    for elemento in lista3[1:]:
        if elemento != elemento_anterior:
    		lista3_sem_duplicadas.append(elemento)
            elemento_anterior = elemento
            
    return lista3_sem_duplicadas