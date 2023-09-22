def hashtag(s):
    '''função que retorna hashtag no início,meio e fim da string
    assinatura: str > str
    casos de teste: hashtag('bem') ==#b#em#
    hashtag('para') ==#pa#ra#
    hashtag('feliz') ==#fe#liz#'''
   return '#' + str(s[0:len(s)//2]) + '#' + str(s[len(s)//2:]) + '#'