def hashtag(str1):
    '''str-> str'''
    str1[:len(str1)//2]
    str1[len(str1)//2:]
    str = '# + str1[:len(str1)//2] + # + str1[len(str1)//2:] + #'
    return str()