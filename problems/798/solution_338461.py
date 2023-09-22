def freq_palavras(frases):
    '''it returns a dictionary with words of text like keys and how many these words looks in text like the keys'value
    string ->dictionary'''
    di={}
    phases=frases
    word=''
    for letter in phases:
        if letter==' ':
            if not word in di:
                di[word]=1
            elif word in di:
                di[word]=di[word]+1
            word=''
        elif not letter==' ':
            word+=letter
    if not word in di:
        di[word]=1
    elif word in di:
        di[word]=di[word]+1
    return di