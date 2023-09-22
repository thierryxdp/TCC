"""Coloca uma "#" no inicio, no meio e no final da string escolhida
assinatura: string -> string """
def hashtag(s):
    inicio = s[ :len(s)//2]
    final = s[len(s)//2: ]
                  
                  return "#" + inicio + "#" + final + "#"