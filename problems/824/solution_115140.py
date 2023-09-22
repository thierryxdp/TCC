def uppCons(frase):
    '''Função que, dada uma frase, retorne a frase com
    todas as suas consoantes em maiúculas(os demais 
    caracteres exatamente como estavam na frase
    str --> str'''    

    i = 0
    frase2 = []
    while i < len(frase):
        if str.lower(frase[i]) in "bcdfghjklmnpqrstvxywzç":
            list.append(frase2, str.upper(frase[i]))
        else:
            list.append(frase2, frase[i])
        i = i + 1
    return str.join("", frase2)