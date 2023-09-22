def inverte(frase):
    'retira as pontuações da frase'
	string_nao_pontuada = frase.replace('!',' ')
	string_nao_pontuada = string_nao_pontuada.replace('?',' ')
	string_nao_pontuada = string_nao_pontuada.replace('!',' ')
	string_nao_pontuada = string_nao_pontuada.replace('...',' ')
    string_nao_pontuada = string_nao_pontuada.replace('-',' ')
    string_nao_pontuada = string_nao_pontuada.replace(':',' ')
    string_nao_pontuada = string_nao_pontuada.replace('.',' ')
    string_nao_pontuada = string_nao_pontuada.split()
    string_nao_pontuada = ','.join(string_nao_pontuada[::-1])
    string_nao_pontuada = string_nao_pontuada.replace(',',' ')
    string_nao_pontuada.lower()
    return string_nao_pontuada