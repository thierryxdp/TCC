def lingua_p(palavra):
    """funcao que dada uma palavra retorna a palavra com p entre as vogais; str->str"""
    contador=0
    nova=''
    palavra=str.lower(palavra)
    for letra in palavra:
        if palavra[contador] in 'aeiouáéíóúã':
            nova+=palavra[contador]+'p'+palavra[contador]
        if palavra[contador] not in 'aeiouáéíóúã':
            nova+=palavra[contador]
        contador+=1
    return nova