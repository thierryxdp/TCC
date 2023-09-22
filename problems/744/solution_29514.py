# Função que recebe uma string e insere o caractere "#" no início no meio e no final
# s é uma string
# str-> str
def hashtag(s):
    x=(len(s))//2
    return "#"+s[0]+"#"+s[x:]+"#"