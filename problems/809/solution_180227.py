# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que trocas os valores das listas de entrada e retorna uma nova lista com a concatenação delas
       list,list→list"""
    l3=lista1+lista2
	l3[1]= lista2[0]
    l3[2]= lista1[1]
    l3[3]= lista2[1]
    l3[4]= lista1[2]
    return l3