def uppCons(frase):
    """Retorna a frase com todas as suas consoantes em maísculas.
    string --> string"""
    
    frase_maiscula = str.upper(frase)
    frase_lista = list(frase_maiscula)
    lista_final = []
    i = 0
        
    while i < len(frase_lista):
        if 'A' == frase_lista[i]:
            list.append(lista_final, 'a')
        elif 'E' == frase_lista[i]:
            list.append(lista_final, 'e')
        elif'I' == frase_lista[i]:
            list.append(lista_final, 'i')
        elif 'O' == frase_lista[i]:
            list.append(lista_final, 'o')
        elif 'U' == frase_lista[i]:
            list.append(lista_final, 'u')
        else:
            list.append(lista_final, frase_lista[i])
        i = i + 1
    
    
    return str.join('', lista_final)