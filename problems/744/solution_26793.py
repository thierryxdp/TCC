# Escreva uma fun¸c˜ao que receba uma string e insira o caractere ”#”
# no in´ıcio, no meio e no final dela. Por exemplo, se a entrada for ”abcd”,
# a sa´ıda deve ser ”#ab#cd#”. Outro exemplo: se receber ”abcde”,
# a fun¸c˜ao deve retornar ”#ab#cde#”.
# str-> str

def hashtag(str1):
    
    #pre = str1[:len(str1)//2]
    #pos = str1[len(str1)//2:]
    #str1 = "#" + pre + "#" + pos + "#"
    str1 = "#" + str1[:len(str1)//2] + "#" + str1[len(str1)//2:] + "#"
    return str1