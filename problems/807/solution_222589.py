def conta_frases(texto):
    '''função que recebe um texto em string e retorna o número de frases desse
texto, as frases são terminadas em '.','!','?' ou '...'; str->int'''

    texto2= str.replace(texto,'...','#')
    texto3= str.replace(texto2, '.', '#')
    texto4= str.replace(texto3,'!','#')
    texto5= str.replace(texto4,'?','#')
    lista= str.split(texto5,'#')

    return len(lista)-1