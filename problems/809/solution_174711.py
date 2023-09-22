# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """ A funcao concatena duas listas: lista1 e 
        lista 2, intercalando seus elementos;
        list, list -> list"""
    separando1=str.split(lista1)
    separando2=str.split(lista2)
    juntandolist= separando1 + separando2
    return juntandolist