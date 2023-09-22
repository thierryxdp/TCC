def inverte (frase):
    """ dada uma frase, retira as letras maiusculas e os carcteres de pontuacao, e retorna a frase com as palavras na ordem invertida
    	:parametro frase: str
        :return: str"""
    frase = str. replace(frase, '-', ' ')
    frase = str. replace(frase, ',', ' ')
    frase = str. replace(frase, ':', ' ')
    frase = str. replace(frase, ';', ' ')
    frase = str. replace(frase, '.', ' ')
    frase = str. replace(frase, '!', ' ')
    frase = str. replace(frase, '?', ' ')
    frase = str. replace(frase, '...', ' ')
    frase = frase.lower()
    frase = str.split(frase)
    list.reverse(frase)
    return str.join(' ', frase)