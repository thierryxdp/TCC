def hashtag(str1):
    '''receba uma string e insira o caractere "#" no inicio, no meio e no fim'''
    '''str-> str'''
    str1[:len(str1)//2]
    str1[len(str1)//2:]
    str = ("#" + str1[:len(str1)//2] + "#" + str1[len(str1)//2:] + "#")
    return str1()