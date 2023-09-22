def retira_pontuacao(entrada):
    separador = ['.','…','!','?','-',',',':',';']


	for j in separador:
    	entrada = entrada.replace(j, ' ')
    return entrada

def inverte(entrada):
    lista = str.split(retira_pontuacao(entrada))
    lista.reverse()
    string = ''
    for termo in lista:
        string += termo
    return str.lower(string)