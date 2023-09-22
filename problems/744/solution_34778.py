def hashtag(s):
    # adicionar # em locais da palavra de entrada / string -> string
    tamanho = len(s)
    metade = tamanho/2
    new_string = '#'+s[:1]+'#'+s[:metade]+'#'
    return new_string