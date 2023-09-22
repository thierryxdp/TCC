def uppCons(phrase):
    new_phrase=''
    i=0
    while i<len(phrase):
        letter=phrase[i]
        if letter.lower() in 'bcdfghjklmnpqrstvwyz':
            letter=letter.upper()
            new_phrase+=letter
            i+=1
            return new_phrase