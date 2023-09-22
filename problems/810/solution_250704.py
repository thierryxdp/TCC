def inverte(frase):
    '''Inverte a ordem das palavras de uma frase;
    entrada: str;
    saída: str;
    '''
    frasesempontuacao = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase, '...',' '),'-',' '), '.', ' '),':', ' '),';', ' '), '?', ' '), '!', ' '),',', ' ')
    listafrase= str.split(frasesempontuacao)
    list.reverse(listafrase)
    frasereversa = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str(listafrasereversa), "',", ''), '",', ''), ' "', ' '), " '", ' '), "['", ''), '["', ''), '"]', ''), "']", '')
    frasefinal = str.lower(frasereversa)
    return frasefinal