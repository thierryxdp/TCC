def uppCons(frase):
    '''funcao que dada uma frase, retorna a frase com todas as suas consoantes maiusculas e os demais caracteres
       exatamente como na frase original
       string -> string '''
    i = 0
    modificada = ''
    while(i < len(frase)):
        if(frase[i] not in 'aeiou'):
            frase = str.upper(frase)
            modificada = modificada + frase[i]
        else:
            frase = str.lower(frase)
            modificada = modificada + frase[i]
        i += 1
    return modificada