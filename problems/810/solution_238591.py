def inverte(frase):
    '''função que dada uma frase retorna outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiusculas e sem pontuação:str->str'''
    filtro1= str.replace(frase,'-',' ')
    filtro2= str.replace(filtro1,':',' ')
    filtro3= str.replace(filtro2,';',' ')
    filtro4= str.replace(filtro3,'!',' ')
    filtro5= str.replace(filtro4,'?',' ')
    filtro6= str.replace(filtro5,',',' ')
    filtro7= str.replace(filtro6,'.',' ')
    
    minuscula= str.lower(filtro7)
    lista_palavra= str.split(minuscula)
    lista_inversa= lista_palavra[::-1]
    
    return (' ',lista_inversa)