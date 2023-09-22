def repetidos(l):
    '''it returns how many times a number and its predecessor are the same
    list -> int'''
    tim=0
    index=0
    while index<len(l):
        if l[index]==l[index-1]:
            tim+=1
            index+=1
        else:
            index+=1
    return tim