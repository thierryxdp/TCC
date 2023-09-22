# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que recebe duas listas, de 3 elementos cada, e 
    	retorna uma outra lista composta dos elementos da primeira
        intercalados comos da segunda
        list,list ->list"""
    lista3=[None]*6
    lista3[::2]=list.copy(lista1)
    lista3[1::2]=list.copy(lista2)
    return lista3