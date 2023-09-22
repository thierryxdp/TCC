def retira_pontuacao(entrada):
    separador = ['.','…','!','?','-',',',':',';']


	for j in separador:
    	entrada = entrada.replace(j, ' ')
    return entrada

def inverte(entrada):
    lista = list.reverse(str.split(retira_pontuacao(entrada)))
    a = len(lista)
    for x in range(a):
        return lista[x] + ' '