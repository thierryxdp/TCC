def hashtag(s):
    '''Adiciona um # no inicio meio e fim de uma string s'''
    return str('#')+s[:len(s)//2]+str('#')+s[len(s)//2:]+str('#')