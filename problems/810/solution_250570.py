def inverte(frase):
    '''Inverte a ordem das palavras de uma frase;
    entrada: str;
    saída: str;
    '''
    frasesempontuacao = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase, '...',' '),'-',' '), '.', ' '),':', ' '),';', ' '), '?', ' '), '!', ' '),',', ' ')
    listafrase= str.split(frasesempontuacao)
    listafrasereversa = listafrase[::-1]
    frasereversa = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str(listafrasereversa), "',", ''), '",', ''), ' "', ' '), " '", ' '), "['", ''), '["', ''), '"]', ''), "']", '')
    frasefinal = str.lower(frasereversa)
    return frasefinal