def retira_pontuacao(frase):

    """Função que dado uma frase retorna a frase com espaços no lugar dos caracteres de pontuação. str -> str"""

	f = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '),'!',' '),'?',' '),';',' '),':',' '),',',' '),'-',' ')

    return f

def inverte(frase):

    """Função que dado uma frase inverte a ordem das palavras da mesma. str -> str"""

    

    f = retira_pontuacao(frase)

    f1 = str.split(f, " ")

    f2 = str.join(" ",f1[::-1])

    f3 = str.replace(f2,'  ',' ')

    return str.lstrip(str.lower(f3))