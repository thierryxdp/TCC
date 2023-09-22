def lingua_p(frase: str)-> str:
    """ Função que receba como parametro uma palavra e retorne esta mesma palavra traduzida para a 
    lingua do P quando,após cada vogal da palavra original, é inserida a sequencia de letras p mais vogal"""
    frase_modificada = list()
    i=0
    
    while(i<len(frase)):
        if(str.lower(frase[i]) in "aeiou"):
            list.append(frase_modificada,frase[i] + 'p')
        else:
            list.append(frase_modificada, frase[i])
        i +=1
     
    return ''.join(frase_modificada)