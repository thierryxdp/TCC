def hashtag(s):
    """Retorna uma string incluindo o símbolo # no início, meio e fim do parâmetro de entrada;
    str->str"""
    return '#'+s[:int(len(s)//2)]+'#'+s[int(len(s)//2):]+'#'