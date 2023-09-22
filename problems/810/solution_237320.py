#INVERTE AS FRASES
def retira_pontuacao(frase):
    'retira as pontuações da frase'
	string_nao_pontuada = frase.replace('!',' ')
	string_nao_pontuada = string_nao_pontuada.replace('?',' ')
	string_nao_pontuada = string_nao_pontuada.replace('!',' ')
	string_nao_pontuada = string_nao_pontuada.replace('...',' ')
    string_nao_pontuada = string_nao_pontuada.replace(',',' ')
    string_nao_pontuada = string_nao_pontuada.replace('-',' ')
    string_nao_pontuada = string_nao_pontuada.replace(':',' ')
    string_nao_pontuada = string_nao_pontuada.replace('.',' ')
    return string_nao_pontuada
def frase_invertida(frase):
    '''inverte a ordem da(s) frase(s)'''
    frase.lower()
    return frase