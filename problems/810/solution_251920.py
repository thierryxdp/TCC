def retira_pontuacao(entrada):
    separador = ['.','…','!','?','-',',',':',';']


	for j in separador:
    	entrada = entrada.replace(j, ' ')
    return entrada

def inverte(entrada):
    lista = str.split(retira_pontuacao(entrada))
    nlista = list.reverse(lista)
    a = len(nlista)
    for x in range(a):
        return lista[x] + ' '