"""funcao que retorna um string com # no inicio meio e fim""""
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    #pre = s[:len(s)//2]
    #pos = s[len(s)//2:]
    #s = "#" + pre + "#" + pos + "#"
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s