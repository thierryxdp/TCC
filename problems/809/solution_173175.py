# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função para intercalar os elementos de duas listas de 3 elementos.
       Onde: "lista1" - é a primeira lista;
             "lista2" - é a segunda lista.
    list, list -> list"""
    lista3 = [lista1[0]] + [lista2[0]] + [lista1[1]] + [lista2[1]] + [lista1[2]] + [lista2[2]]
    return lista3