# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    pre = str[:len(str1)//2]
    pos = str[len(str1)//2:]
    str1 = "#" + pre + "#" + pos + "#"
    str1 = "#" + str1[:len(str1)//2] + "#" + str1[len(str1)//2:] + "#"
    return str1