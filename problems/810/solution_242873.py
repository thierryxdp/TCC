def retira_pontuacao(frase):
    '''funcao que recebe uma frase e retorna essa mesma frase sem esses caracteres de pontuacao, substituindo-os por espaço
str -> str'''
    frase=str.replace(frase,'-',' ')
	frase=str.replace(frase,',',' ')
	frase=str.replace(frase,':',' ')
	frase=str.replace(frase,';',' ')
	frase=str.replace(frase,'.',' ')
	frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    return frase
def inverte(frase):
    '''funcao que recebe uma frase e retorna a mesma na ordem inversa sem letras maiusculas
    str -> str'''
    frase=retira_pontuacao(frase)
    frase=frase[-1:]
    return str.lower(frase)