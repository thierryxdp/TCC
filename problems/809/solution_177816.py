# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que retorna um intercalamento entre duas listas"""
    return lista1[:1] + lista2[:1] + lista1[1:2] + lista2[1:2] + lista1[2:3] + lista2[2:3]