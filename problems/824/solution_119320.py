def uppCons(palavra):
    texto= list(palavra)
    index= 0
    letters= []
    
    while index < len(palavra):
        if texto[index] in 'bcdfghjklmnpqrstvwxyzç':
            list.insert(letters,index, texto[index].upper())
            index = index+1
        else:
            list.insert(letters,index, texto[index])
            index = index+1
    return ''.join(letters)