def retira_pontuacao(frase):
    """Função que recebe uma frase e retorna a frase sem 
    caracteres de pontuação"""
	f = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '),'!',' '),'?',' '),';',' '),':',' '),',',' '),'-',' ')
    return f
def inverte(frase):
    """Função que recebe uma frase e inverte a ordem das palavras"""
    
    f = retira_pontuacao(frase)
    f1 = str.split(f, " ")
    f2 = str.join(" ",f1,-1)
    return f2