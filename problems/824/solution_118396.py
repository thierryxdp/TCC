def uppCons(phrase):
    new_phrase = ''
    for letter in phrase.upper():
        if letter in 'AEIOU':
            new_phrase += letter.lower()
        else:
            new_phrase += letter