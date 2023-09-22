def inverte(frase):
    'retira as pontuações da frase'
	string_nao_pontuada = frase.replace('!',' ')
	string_nao_pontuada = string_nao_pontuada.replace('?',' ')
	string_nao_pontuada = string_nao_pontuada.replace('!',' ')
	string_nao_pontuada = string_nao_pontuada.replace('...',' ')
    string_nao_pontuada = string_nao_pontuada.replace(',',' ')
    string_nao_pontuada = string_nao_pontuada.replace('-',' ')
    string_nao_pontuada = string_nao_pontuada.replace(':',' ')
    string_nao_pontuada = string_nao_pontuada.replace('.',' ')
    string_nao_pontuada = string_nao_pontuada.split()
    string_nao_pontuada = string_nao_pontuada.join[-1]
    return string_nao_pontuada