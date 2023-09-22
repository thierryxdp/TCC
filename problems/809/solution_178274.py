'retorna a intercalação de duas listas'
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    return [*sum(zip(lista1,lista2),())]