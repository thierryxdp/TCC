def hashtag(s):
    # adicionar # em locais da palavra de entrada / string -> string
    tamanho = len(s)
    metade = tamanho/2
    '#'+s[:1]+'#'+s[:metade]+'#'