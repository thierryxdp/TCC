def hashtag(s):
    "Função que insere o caractére # no inicio, meio e fim de uma string"
    pre = s[:len(s)//2]
    pos = s[len(s)//2:]
    s = "#" + pre + "#" + pos + "#"
    
    return s