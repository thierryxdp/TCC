def hashtag(s):
    '''escreva uma funcao que receba uma string e insira '#' no inicio, meio e fim'''
    meio=s[:len(s)//2]
    fim=s[len(s)//2:]
    return '#'+meio+'#'+fim+'#'