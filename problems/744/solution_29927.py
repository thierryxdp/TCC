def hashtag(string):
    '''Retorna uma string inserindo '#' no início, meio e fim da mesma.
       str -> str'''
    string1 = string[:len(string)//2]
    string2 = string[(len(string)//2):]
    return '#'+string1+'#'+string2+'#'