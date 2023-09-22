# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função dar duas listas de tamanho 3 (exemplo: L1 = [1,3,5]) e retorna uma nova lista formada intercalando os elementos das duas listas
       Parametros: list -> list """
    nova_lista = [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    return nova_lista