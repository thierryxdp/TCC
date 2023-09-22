def conta_frases(text):
    '''Given a text as parameter, the function returns
    the number of phrases inside it.
    Str --> int'''
    TXTwithoutExclamation = str.replace(text, '!', '.')
    TXTwthtExcAndInterrogation = str.replace(TXTwithoutExclamation, '?', '.')
    TXTwthtExcAndIntAndThreeDots = str.replace(TXTwthtExcAndInterrogation, '...', '.')
    numberOfPhrases = str.count(TXTwthtExcAndIntAndThreeDots, '.')
    return numberOfPhrases