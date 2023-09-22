def hashtag(s):
    """Função que entra uma string e retorna string com os caracteres # no início,meio e fim"""
 	meio=len(s)//2
    s='#'+s[:meio]+'#'+s[meio:]+'#'
    return s