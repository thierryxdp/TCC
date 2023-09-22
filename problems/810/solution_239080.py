def inverte(nova_frase):
    '''Função que dada uma frase como entrada retorne uma 
    outra com as mesmas palavras mas em ordem inversa e sem
    pontuação e letras maiúsculas.
    string --> string'''
    def retira_pontuacao(frase):
        frase = frase.replace(";"," ")
    	frase = frase.replace("-"," ")
    	frase = frase.replace("!"," ")
    	frase = frase.replace("?"," ")
    	frase = frase.replace(","," ")
    	frase = frase.replace(":"," ")
    	frase = frase.replace("."," ")
    	frase
    nova_frase = str.lower(nova_frase)
    lista = str.split(nova_frase)
    nova_lista = lista[::-1]
    return str.join("",nova_lista)