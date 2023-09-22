def hashtag(s):
    '''a funcao recebe um "#" no começo meio e fim da palavra'''
    '''str->str'''
    meio=len(s)//2
    return '#'+str(s[0:meio])+ '#'+ str(s[meio:]) + '#'