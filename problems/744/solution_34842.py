"""Retorna a string escolhida com uma "#" em seu inicio meio e fim
assinatura: string -> string"""
def hashtag(s):
    pre = s[ :len(s)//2]
    pos = s[len(s)//2: ]
    
    return "#" + pre + "#" + pos + "#"