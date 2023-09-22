def hashtag(s):
'''função que insere a caractere # no início, meio e fim da string
str-> str'''
 #pre = s[:len(s)//2]
#pos = s[len(s)//2:]
#s = "#" + pre + "#" + pos + "#"
s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
return s