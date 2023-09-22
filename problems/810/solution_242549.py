def inverte(texto):
    '''função que recebe um texto de entrada em formato string, retira sua pontuação e inverte a ordem das palavras;string->string''' 
    texto=str.split(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(texto,'-',' '),',',' '),':',' '),'.',' '),'?',' '),'!',' '))
    list.reverse(texto)
    return str.lower(str.replace(str.replace(str.strip(str.strip(str(texto),'['),']'),',',''),"'",''))