def hashtag(s):
    '''retorna a string acrescida de # no inicio,meio e final da mesma'''
    '''str->str'''
    meio = (len(s))//2
    return '#'+ s[:(meio)]+ '#'+ s[(meio):]+ '#'