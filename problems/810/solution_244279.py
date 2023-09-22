def retira_pontuacao(frase):
    ''' A função substitui caracteres de pontuação de uma frase por espaços.
    Retornando a frase editada.
    	str -- > str'''
    
    caracteres = ['-',',','.',';',':','?','...','!']
    for i in caracteres:
        frase = frase.replace(i, ' ')
    return frase


def inverte(frase):
    sem_pontuacao = retira_pontuacao(frase)
    minusculo = sem_pontuacao.lower()
    lista = minusculo.split()
    list.reverse(lista)
    frase_invertida = str.join(' ',lista)
    return frase_invertida

 #Não entendi o motivo do erro que estava sendo apresentado anteriormente