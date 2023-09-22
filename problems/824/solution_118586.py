def uppCons(frase):
    '''retorna uma string com as consoantes que apareceram em um texto,
    maiusculas
    str->str'''
    i=0
    consoantes=''
    while i<len(frase):
        if texto[i] in 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'):
            consoantes=consoantes+frase[i]
        i=i+1
    return consoantes