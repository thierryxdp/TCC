def filtro(tupla):
#Função recebe uma tupla e retorna
#Uma nova tupla apenas com os elementos que são pares
#da tupla original.
# tupla --> tupla
	novaTupla = []
	for n in tupla:
        if n%2 == 0:
            lista.append(n)
	
    return tuple(novaTupla)