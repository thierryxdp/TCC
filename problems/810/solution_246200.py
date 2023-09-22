def retira_pontuacao(frase):
    """ remove toda a pontuação de uma dada frase """
    new_string = frase
    to_remove = ['-',':',';','.','?','!',',']
    for x in to_remove:
        new_string = new_string.replace(x, ' ')
        return new_string
    
    
def inverte(frase):
    """ dada uma função que retorna o inverso de uma lista, removendo a pontuação e deixando as palavras em minusculas """
    lista = retira_pontuacao(frase).split()
    invertida = lista.reverse()
    invertida_str = ','.join(invertida)
    return retira_pontuacao(invertida_str)