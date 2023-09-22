def inverte(frase):
    '''esta e a funçao inverte que dado uma frase retorna a mesma frase na ordem inversa e sem letras maiusculas
    	str -> str'''
    frase = str.replace(frase,";","")
    frase = str.replace(frase, "-"," ")
    frase = str.replace(frase, "!","")
    frase = str.replace(frase, "?","")
    frase = str.replace(frase, ",","")
    frase = str.replace(frase, ":","")
    frase = str.replace(frase, ".","")
    
    nova_frase = str.lower(frase)
    
    lista = str.split(nova_frase, ' ')
    
    nova_lista = lista[::-1]