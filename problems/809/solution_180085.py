# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Gera uma lista que é formada intercalando os elementos da Lista1 e Lista2
    string, string -> string"""
    return lista1[:1]+lista2[:1]+lista1[1:2]+lista2[1:2]+lista1[2:3]+lista2[2:3]