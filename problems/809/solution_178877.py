# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Funcao lista 3 que intercala duas listas de tres parametros
       cada um lista 1 e lista2
       list->list"""
    return [*sum(zip(lista1,lista2),())]