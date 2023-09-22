def uppCons(frase):
    """Retorna a frase com todas as suas consoantes em maísculas.
    string --> string"""
    
    frase_maiscula = str.upper(frase)
    frase_lista = list(frase_maiscula)
    lista_final = []
    i = 1
        
    while i < len(frase_lista):
        if frase_lista[i] in 'AEIOUÁÉÍÓÚÃÕÂÊÎÔÛ':
            list.append(lista_final, str.lower(frase_lista[i]))
        else:
            list.append(lista_final, frase_lista[i])
        i = i + 1
    
    
    
    return lista_final