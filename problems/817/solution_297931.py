def acima_da_media(lista):
    '''...'''
    
    list1 = sum(lista)
    list2 = len(lista)
    list3 = list1/list2
    
    if list3 in list:
        list.remove(list3)
        list.append(list3)
        list.sort()
        
        return list[(list.index(list3)+1):]