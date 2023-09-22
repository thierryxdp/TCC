def hashtag(str1):
    """retorne a string de entrada com o formato de #no início, no meio e no final da string"""
     str1 = "#" + str1[:len(str1)//2] + "#" + str1[len(str1)//2:] + "#"
        return str1