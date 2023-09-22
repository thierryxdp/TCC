def inverte(frase):
    frase1 = str.replace(frase, "-", " ")
    frase2 = str.replace(frase1, ",", " ")
    frase3 = str.replace(frase2, ":", " ")
    frase4 = str.replace(frase3, ";", " ")
    frase5 = str.replace(frase4, ".", " ")
    frase6 = str.replace(frase5, "!", " ")
    frase7 = str.replace(frase6, "?", " ")
    
    frase8 = str.lower(frase7)'Defini minusculo'
    lista = str.split(frase8) 'transforma string em lista'
    list.sort(lista) 'altera a ordem da lista'
    new_frase = str.join(" ", lista)'concatena os elemntos da lista em string'
    
    return new_frase