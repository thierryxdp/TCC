def hashtag(insta):
"""Recebe uma string e adiciona um caracter no inicio e no final da mesma"""
""" insta"""
""" str-> str """
    
    str1 = insta
    str2 = "#"
    return str2 + str1[0:int(len(str1)/2)] + str2 + str1[int(len(str1)/2):len(str1)+1] + str2