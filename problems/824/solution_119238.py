def uppCons(text):
    '''it returns the text with its all consonants in capital letters
    string ->string'''
    new=''
    index=0
    alphabet={'b':'B','c':'C','ç':'Ç','d':'D','f':'F',
              'g':'G','h':'H','j':'J','k':'K',
              'l':'L','m':'M','n':'N','p':'P',
              'q':'Q','r':'R','s':'S','t':'T',
              'v':'V','w':'W','x':'X','y':'Y','z':'Z'}
    while index<len(text):
        if text[index] in 'AEIOUaeiou':
            new+=text[index]
            index+=1
        elif not text[index] in alphabet and 'AEIOUaeiou':
            new+=text[index]
            index+=1
        else:
            new+=alphabet[text[index]]
            index+=1
    return new