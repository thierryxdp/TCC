def uppCons(Phrase):
    '''Function that turns all the consonants of a given 
    phrase into upper case and leaves the rest as it was, 
    without any change. Give, as parameter, the phrase.
    Str --> Str.'''
    index = 0
    NewPhrase = ''
    while index != len(Phrase):
        if Phrase[index] in 'bcçdfghjklmnpqrstvwxyz':
            UpperConsonant = str.upper(Phrase[index])
            NewPhrase = NewPhrase + UpperConsonant
        else:
            NewPhrase = NewPhrase + Phrase[index]
        index = index + 1
    return NewPhrase