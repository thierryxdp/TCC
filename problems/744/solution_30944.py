def hashtag(s):
    m=len(s)//2 #descobre o meio aproximado da string
    nova_string="#"+s[0:m]+"#"+s[m:]+"#" #cria uma nova string concatenando # entre os elementos de s
    return nova_string