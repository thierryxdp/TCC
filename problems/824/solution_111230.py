def uppCons(frase):
    """Retorna a frase com todas as suas consoantes em maísculas.
    string --> string"""
    
    frase_maiscula = str.upper(frase)
    frase_lista = list(frase_maiscula)
    lista_final = []
    i = 0
        
    while i < len(frase):
        if 'A' or 'E' or 'I' or 'O' or 'U' in frase_lista[i]:
            list.append(lista_final, str.lower(frase_lista[i]))
        else:
            list.append(lista_final, frase_lista)
        i = i + 1
    return str.join('', lista_final)