# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    pre = str[:len(str)//2]
    pos = str[len(str)//2:]
    str = "#" + pre + "#" + pos + "#"
    str = "#" + str[:len(str1)//2] + "#" + str[len(str1)//2:] + "#"
    return str