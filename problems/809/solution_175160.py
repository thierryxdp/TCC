'''Função que recebe duas listas de tamanho 3 e retorna uma terceira
	lista com os elementos das duas listas de entrada intercalados.
    As listas de entrada da função devem, obrigatoriamente, ser 
    inseridas entre colchetes (ex:[a,b,c]).
    list -> list'''
def intercala(lista1, lista2):
    return [lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]