def hashtag(s):
   '''função que posiciona o caractere '#' no meio no inicio e no fim de uma string s
    entrada:str
    saída:str'''
    #pre = str1[:len(str1)//2]
    #pos = str1[len(str1)//2:]
    #str1 = "#" + pre + "#" + pos + "#"
    str1 = "#" + str1[:len(str1)//2] + "#" + str1[len(str1)//2:] + "#"
    return str1