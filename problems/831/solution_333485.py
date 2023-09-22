def lingua_p(palavra):
    for a in palavra:
        if a == 'a'or'e'or'i'or'o'or'u'or'á'or'é'or'í'or'ó'or'ú':
            palavraa = palavra.replace(a,a+'p'+a)
            return(palavraa)