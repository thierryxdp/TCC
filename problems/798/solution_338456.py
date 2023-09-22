def freq_palavras(frases):
    '''it returns a dictionary with words of text like keys and how many these words looks in text like the keys'value
    string ->dictionary'''
    dic={}
    phases=frases
    word=''
    for letter in phases:
        if letter==' ':
            dic[word]=dic[word]+1
            word=''
        elif not letter==' ':
            word+=letter
    return dic