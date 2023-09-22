def retira_pontuacao(texto):
    '''Retorna a frase com todos os caracteres substituidos por espaço
    assinatura str -> str'''
    separador = ['.','!','?','-',',',':',';']
    novastring = ''
    for x in range(len(texto)):
        if texto[x] in separador and texto[x-1] not in separador and texto[x-2] not in separador: 
                novastring += str.replace(texto, separador, ' ')
        if texto[x] in separador:
                novastring += str.replace(texto, separador, ' ')
    return novastring