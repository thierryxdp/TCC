#Funçao que recebe uma string e insere o caractere hashtag # no inicio, meio e no final dela.
#str->str
def hashtag(s):
    meio=(len(s)//2)
    parte1=s[0:meio]
    parte2=s[meio:len(s)]
    return '#'+ parte1 + '#' + parte2 + '#'