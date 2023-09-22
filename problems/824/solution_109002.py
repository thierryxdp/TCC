def uppCons(frase):
    """Dada uma frase essa função retorna a frase com todas as consoantes em maíusculo; string -> string"""
    contador = 0
    frase_nova = ''
  
    while contador < len(frase):
        if frase[contador] in 'bcdfghjklmnpqrstvwxyzç':
            elemento = str.upper(frase[contador])
        else:
            elemento = frase[contador]
            
        frase_nova = frase_nova + elemento
        contador = contador + 1
        
    return frase_nova