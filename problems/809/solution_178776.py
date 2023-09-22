# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    resultado = []
    i = 0
    
	while i<len(lista1+lista2):
        resultado.append(lista1[i])
        resultado.append(lista2[i])
        i += 1
    return resultado