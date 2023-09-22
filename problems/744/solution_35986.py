def hashtag(str1):
   '''função que posiciona o caractere '#' no meio no inicio e no fim de uma string s
    entrada:str
    saída:str'''
    str1="#"+str1[:len(str1)/2]+"#"+str1[len(str1)/2:]+"#"
    return str1