def inverte (frase):
    '''Não foi possível pegar a função do exercício anterior
    por isso refiz a primeira parte dentro da própria função.
    Com a função split(), a string se separa em palavras a
    partir dos espaços, retornando uma lista. A função reverse()
    inverte a ordem dos elementos dessa lista. a função join()
    concatena os elementos em uma string e lower() converte
    todas as letras da string em minúsculas.
    str, list >> str
    '''
    
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '...', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, '-', ' ')
    
    frase = str.split(frase)
    list.reverse(frase)
    frase = str.join(' ', frase)
    frase = str.lower(frase)
    return(frase)