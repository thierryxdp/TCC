"""calcula e retorna uma string com # no começo, no meio e no fim
str-> str"""
def hashtag(s):
    if '#'==0:
        return '#'+s
    if 0>'#'>len(s):
        return s([0:'#'])+s(['#':len(s)])
    if '#'==len(s):
        return s+"#"