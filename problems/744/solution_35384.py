def hashtag(s):
    '''Função que coloca a # no meio da palavra'''
    palavra=s
    total=len(palavra)
    meio=total//2
    meiozinho=int(meio)
    frente=int(meiozinho+1)
    return '#'+palavra[:meio]+'#'+palavra[meio:]+'#'