def lingua_p(frase):
    """Função que recebe uma palavra como parametro e me retorna a mesma palavra traduzida para lingua P
str->str"""
    frase=str.lower(frase)
    texto=''
    for i in frase:
        if i in "aeiouáéíóú":
            texto+=i+'p'+i
            
        if i not in "aeiouáéíóú":
            texto+=i
    return texto