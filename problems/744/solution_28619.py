# Escreva uma fun¸c˜ao que receba uma string e insira o caractere ”#”
# no in´ıcio, no meio e no final dela. Por exemplo, se a entrada for ”abcd”,
# a sa´ıda deve ser ”#ab#cd#”. Outro exemplo: se receber ”abcde”,
# a fun¸c˜ao deve retornar ”#ab#cde#”.
# str-> str
def hashtag(s):
    #pre = s[:len(s)//2]
    #pos = s[len(s)//2:]
    #s = "#" + pre + "#" + pos + "#"
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s