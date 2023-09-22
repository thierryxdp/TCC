# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que retorna a intercalação de duas listas, retornando uma terceira lista com os elementos das listas 1 e 2. Entrada -> int, int, int. Saída -> int, int, int"""
    return([lista1[0]] + [lista2[0]] + [lista1[1]] + [lista2[1]] + [lista1[2]] + [lista2[2]])