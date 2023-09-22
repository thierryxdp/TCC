def hashtag(texto):
    """Recebe uma string e insere o caractere # no início, no meio e no final dela; str->str"""
    return '#'+str(texto[0:len(texto)//2])+'#'+str(texto[len(texto)//2:])+'#'