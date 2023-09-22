def retira_pontuacao(entrada):
    separador = ['.','…','!','?','-',',',':',';']


	for j in separador:
    	entrada = entrada.replace(j, ' ')
    return entrada

def inverte(entrada):
    lista = list.reverse(str.split(retira_pontuacao(entrada)))
    for x in range(len(lista)):
        return lista[x] + ' '