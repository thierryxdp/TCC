def inverte(Frase):
    '''Função que dada uma frase como entrada retorne uma 
    outra com as mesmas palavras mas em ordem inversa e sem
    pontuação e letras maiúsculas.
    string --> string'''
    frase = frase.replace(";"," ")
    frase = frase.replace("-"," ")
    frase
    frase = frase.replace("!"," ")
    frase = frase.replace("?"," ")
    frase
    frase = frase.replace(","," ")
    frase = frase.replace(":"," ")
    frase
    frase = frase.replace("."," ")
    nova_frase = str.lower(frase)
    lista = str.split(nova_frase,'')
    nova_lista = lista[::-1]
    return str.join("", nova_lista)