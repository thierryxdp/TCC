def inverte(frase):
    """retorna a frase invertida,sem pontuação e sem letras maiúsculas"""
    frase1 = str.lower(frase)   #retorna a string em letras minúsculas.
    frase2 = str.replace(frase1, '-' , ' ')
    frase3 = str.replace(frase2, '.' , ' ')
    frase4 = str.replace(frase3, '?' , ' ') #retira as pontuações
    frase5 = str.replace(frase4, '!' , ' ')
    frase6 = str.replace(frase5, ',' , ' ')
    frase7 = str.split(frase6)  #retorna uma lista com as substrings da frase
    list.reverse(frase7)        #inverte a ordem dos elementos da lista
    frase8 = ' '.join(frase7)   #concatena as strings da lista 
    return frase8