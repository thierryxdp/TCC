def hashtag(frase):
    fr = frase[0:len(frase)//2]
    ase = frase[len(frase)//2:]
    nova = '#'+fr+'#'+ase+'#'
    return nova