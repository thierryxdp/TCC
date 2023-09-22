def retira_pontuacao(texto):
    '''Retorna a frase com todos os caracteres substituidos por espaço
    assinatura str -> str'''
    separador = ['.','!','?','-',',',':',';']
    novastring = ''
    for x in range(len(texto)):
        for y in separador:
        	if texto[x] in separador and texto[x-1] not in separador and texto[x-2] not in separador: 
                novastring += str.replace(texto, y, ' ')
        	if texto[x] in separador:
                novastring += str.replace(texto, y, ' ')
    return novastring