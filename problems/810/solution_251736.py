def retira_pontuacao(text):
    '''Function that substitutes all the gramatic pounctuations
    by an empty space, and returns it.
    Str --> Str'''
    #Informations:
    #TXTWht = text without
    #D = '-' , C = ',' , TD = ':' , DC = ';' 
    #Dot = '.' , Exc = '!' , Int = '?' , ThreeDots = '...'
    TXTWithouD = str.replace(text, '-', ' ')
    TXTWhtD_C= str.replace(TXTWithouD, ',', ' ')
    TXTWhtD_C_TD = str.replace(TXTWhtD_C, ':', ' ')
    TXTWhtD_C_TD_DC = str.replace(TXTWhtD_C_TD, ';', ' ')
    TXTWhtD_C_TD_DC_Dot = str.replace(TXTWhtD_C_TD_DC, '.', ' ')
    TXTWhtD_C_TD_DC_Dot_Exc = str.replace(TXTWhtD_C_TD_DC_Dot, '!', ' ')
    TXTWhtD_C_TD_DC_Dot_Exc_Int = str.replace(TXTWhtD_C_TD_DC_Dot_Exc, '?', ' ')
    TXTWhtD_C_TD_DC_Dot_Exc_Int_ThreeDots = str.replace(TXTWhtD_C_TD_DC_Dot_Exc_Int, '...', ' ')
    return TXTWhtD_C_TD_DC_Dot_Exc_Int_ThreeDots

def inverte(Text):
    '''Given a text as parameter, this function makes the following procedures:
    - Turns all the uppercase letters into lowercase ones.
    - Remove all the pounctuations.
    - Reverse the phrase from the backward-forward direction to forward-backward.
    Str --> str'''
    onlyLowercaseLetters = str.lower(Text)
    withoutPounctuatuions = retira_pontuacao(onlyLowercaseLetters)
    splittedText = str.split(withoutPounctuatuions)
    list.reverse(splittedText)
    finalText = str.join(' ', splittedText)
    return finalText