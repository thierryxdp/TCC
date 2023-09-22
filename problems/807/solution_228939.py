def conta_frases(texto):
    '''analisa e determina o número de frases existentes no texto
    	str->int'''
    
    texto2=texto.replace('...',' ',-1)
    texto3=texto2.replace('.',' ',-1)
    texto4=texto3.replace('!',' ',-1)
    texto5=texto4.replace('?',' ',-1)
    
    texto_lista=texto5.split('  ')
    
    return len(texto_lista)