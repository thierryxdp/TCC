# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    lista1=str.split(str(lista1))
    lista2=str.split(str(lista2))
    return lista1[0] + str.strip(lista2[0],'[') + lista1[1] + lista2[1] + str.strip(lista1[2],']') + "," + lista2[2]