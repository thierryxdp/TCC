def retira_pontuacao(string):
    '''Função que recebe uma string e retorna ela sem nenhum caracter de pontuação.
    Esses caracteres serão substituídos por espaço. str->str'''
    subs_exclamacao=string.replace('!',' ')
    subs_reticencias=subs_exclamacao.replace('...',' ')
    subs_interrogacao=subs_reticencias.replace('?',' ')
    subs_pontovirgula=subs_interrogacao.replace(';',' ')
    subs_travessao=subs_pontovirgula.replace('-',' ')
    subs_2pontos=subs_travessao.replace(':',' ')
    subs_virgula=subs_2pontos.replace(',',' ')
    string_pronta=subs_virgula.replace('.',' ')
    return string_pronta

def inverte(frase):
    '''Função que recebe uma frase dada como entrada e retorna outra frase que tem
    as mesmas palavras da frase de entrada, porém na ordem inversa, sem letras maiúsculas
    e sem pontuação. Para retirar a pontuação é usada uma outra função chamada retira_pontuacao.
    str->str'''
	frase_sempontuacao=retira_pontuacao(frase)
    palavras_separadas=str.split(frase_sempontuacao)
    list.reverse(palavras_separadas)
    frase_invertida=str.join(' ',palavras_separadas)
    frase_pronta_minuscula= str.lower(frase_invertida)
    return frase_pronta_minuscula