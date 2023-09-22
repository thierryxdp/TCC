def hashtag(s):
    """ Dado uma string vamos retornar essa string com o'#' no inicio, meio e final
        parametros:
        Entrada -> str,str
        Saida   -> str  """
    #metade=len(s)//2
    new_str='#'+s[:len(s)//2]+'#'+s[len(s)//2:]+'#'
    return new_str