# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Funcao que, dadas duas lista com tres elementos, retorna uma terceira lista com elementos intercalados das duas dadas;
    entrada: list, list
    saída: list"""
    inter = lista1 + lista2
    inter [::2] = lista1
    inter [1::2] = lista2
    return inter