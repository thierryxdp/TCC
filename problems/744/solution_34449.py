def hashtag(s):
    '''calcula e retorna a string com # no início, meio e final; str->str'''
    d=len(s)//2
   return '#'+s[0:d]+'#'+s[d: ]+'#'