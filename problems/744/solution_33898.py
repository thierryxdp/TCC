def hashtag(s):
    'dada uma str s, insere # no inicio, meio e fim dela str - > str'
    i=int(len(s)/2)
    m='#'+s[:i]+'#'+s[i+1:]+'#'
    return m