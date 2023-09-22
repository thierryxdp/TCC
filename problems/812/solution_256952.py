#Retira as pontuações e troca por espaço
def retira_pontuacao(frase):
    'retira as pontuações da frase'
	string_nao_pontuada = frases.replace('!',' ')
	string_nao_pontuada = string_nao_pontuada.replace('?',' ')
	string_nao_pontuada = string_nao_pontuada.replace('!',' ')
	string_nao_pontuada = string_nao_pontuada.replace('...',' ')
    string_nao_pontuada = string_nao_pontuada.replace(',',' ')
    string_nao_pontuada = string_nao_pontuada.replace('-',' ')
    string_nao_pontuada = string_nao_pontuada.replace(':',' ')
    return string_nao_pontuada