"""calcula e retorna uma string com # no começo, no meio e no final
str-> str"""
def hashtag(s):
    return str('#')+(s[0:s//2])+('#')+(s[s//2:len(s)])+('#')