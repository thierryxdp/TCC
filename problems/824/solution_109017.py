def uppCons(frase):
    '''funcao que dada uma frase, retorna a frase com todas as suas consoantes maiusculas e os demais caracteres
       exatamente como na frase original
       string -> string '''
    indice = 0
    modificada = ''
    while(indice < len(frase)):
        if(frase[indice] not in 'aeiou'):
            modificada[indice] = str.upper(frase[indice])            
        indice += 1
    return modificada