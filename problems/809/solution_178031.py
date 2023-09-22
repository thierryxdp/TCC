# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """funçao que recebe duas listas e devolve a união delas intercalads;
    int, int -> int"""
	return [sub[item] for item in range(len(lista2))
                      for sub in [lista1, lista2]]