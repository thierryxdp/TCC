def hashtag(s):
    """retorna a string de entrada com o caractere no inicio, no meio e no final dela;
    string -> string"""
    quant_total=len(s)
    return '#'+(s[0:quant_total/2])+'#'+(s[(quant_total/2)+1:])+'#'