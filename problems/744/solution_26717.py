def hashtag(string):
    """Recebe uma string e insere o caractere # no início, no meio e no final dela; str->str"""
    z = len(string)/2
    return '#'+string[0:z]+'#'+string[z:]+'#'