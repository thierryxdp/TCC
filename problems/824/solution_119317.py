def uppCons(palavra):
    texto= list(palavra)
    index= 0
    letters= []
    
    while index < len(palavra):
        if texto[index] in 'bcdfghjklmnpqrstvwxyzç':
            letters.insert(index, texto[index].upper())
            index = index+1
        else:
            letters.insert(index, texto[index].upper())
            index = index+1
    return ' '.join(letters)