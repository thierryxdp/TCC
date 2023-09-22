def inverte(frase):
    
   '''Função que inverte a ordem das palavras da frase dada, sem pontuação e sem letras maiúsculas. str -> str'''

    texto = str.replace(frase,'-',' ')
    texto2 = str.replace(texto,',',' ')
    texto3 = str.replace(texto2,':',' ')
    texto4 = str.replace(texto3,';',' ')
    texto5 = str.replace(texto4,'...',' ')
    texto6 = str.replace(texto5,'?',' ')
    texto7 = str.replace(texto6,'!',' ')
    texto8 = str.replace(texto7,'.',' ')
    
    frase2 = texto8

    frase3 = str.lower(frase2)

    frase4 = str.split(frase2)

    frase5 = list.reverse(frase4)

    frase6 = str.join(' ',frase5)

    return frase6