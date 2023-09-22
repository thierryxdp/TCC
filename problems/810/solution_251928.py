def retira_pontuacao(entrada):
    separador = ['.','…','!','?','-',',',':',';']


	for j in separador:
    	entrada = entrada.replace(j, ' ')
    return entrada

def inverte(entrada):
    lista = str.split(retira_pontuacao(entrada))
    list.reverse(lista)
    string = ''
    for termo in lista:
        if termo != lista[-1]:
            string += termo + ' '
        else:
            string += termo
    return str.lower(string)