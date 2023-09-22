def hashtag(s):
    '''função que coloca hashtags no meio das entradas'''
    str1 = "#" + str1[:len(str1)//2] + "#" + str1[len(str1)//2:] + "#"
    return str1