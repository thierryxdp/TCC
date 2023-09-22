def inverte(frase):
    ''' função que retorna uma frase contendo as mesmas
    	palavras da frase de entrada na ordem invesa, sem
        pontuação e sem letra maiúscula.
        str ---> str '''
    
    sempont = str.replace(frase, '.', ' ')
    sempont = str.replace(sempont, '?', ' ')
    sempont = str.replace(sempont, ',', ' ')
    sempont = str.replace(sempont, '!', ' ')
    sempont = str.replace(sempont, '-', ' ')
    sempont = str.replace(sempont, ':', ' ')
    minuscula = str.replace(sempont, ';', ' ')
    minuscula = str.lower(minuscula)
    inicioinversao = str.split(minuscula)
    list (inicioinversao)
    list.reverse(inicioinversao)
    str(inicioinversao)
    a = str(inicioinversao).strip('[]')
    return a