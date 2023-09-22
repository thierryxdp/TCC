def hashtag(string):
    """Recebe uma string e insere o caractere # no início, no meio e no final dela; str->str"""
    return '#'+string[0:(len(string)/2)]+'#'+string[len((string)/2):]+'#'