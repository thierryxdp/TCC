def hashtag(s):
    """Insere o caractere "#" no início,
meio e fim de uma string.
str-> str
testes:
hashtag("isabella") == '#isab#ella#'
hashtag("daniel") == '#dan#iel#'
hashtag("galo") == '#ga#lo#'
hashtag("python") == '#pyt#hon#'
"""
    #início
    s[: len(s) // 2]
    #fim
    s[len(s) // 2:]
    s =  "#"  +  s[: len(s) // 2 ] +  "#"  +  s[ len(s) // 2 :] +  "#"
    return  s