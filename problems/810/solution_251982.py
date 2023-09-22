def retira_pontuacao(text):
    '''retorna uma string retirando seus caracteres de pontuação
    str -> str'''
    text = str.replace(text,'!',' ')
    text = str.replace(text,'-',' ')
    text = str.replace(text,'?',' ')
    text = str.replace(text,'...',' ')
    text = str.replace(text,',',' ')
    text = str.replace(text,':',' ')
    text = str.replace(text,';',' ')
    text = str.replace(text,'.',' ')
    return text

def inverte(text):
    '''retorna uma frase com as palavras na ordem inversa e sem pontuação, comparada a de entrada
    str -> str'''
    semPontuacao = retira_pontuacao(text)
    semMaiusculas = str.lower(semPontuacao)
	palavras = str.split(semMaiusculas)
    list.reverse(palavras)
    palavras = str.join(' ',palavras)
    return palavras