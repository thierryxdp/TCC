def inverte(frase):
    '''Função que recebe uma frase e retorna a frase com a ordem inversa das palavras, sem letras maiúsculas e sem pontuação'''
	'''str --> str'''

    y = str.replace(frase,"-"," ")
    y1 = str.replace(y,".","")
    y2 = str.replace(y1,"!","")
    y3 = str.replace(y2,",","")
    y4 = str.replace(y3,"?","")
    
    z = str.split(y4,"!")
    z1 = ''.join(z)
    
    x=str.split(z1," ")
    x.reverse()
    x1 = ' '.join(x)
    return str.lower(x1)