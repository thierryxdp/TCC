def hashtag(s):
    """imposta a string, recebe # no inicio,
meio e fim
ex: >>> hashtag('abcd') - #ab#cd#
str -> str"""
    return '#'+str(s[0:len(s)//2])+'#'+str(s[len(s)//2:])+'#'