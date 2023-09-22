def insere(lista_numero, n):
    '''Give an ordered list with intergers, from the smaller to the bigger number,
    and a ramdom number (n) as parameters, respectively. This function
    will put 'n' in the ordered list, without messing with it´s organization.
    list, int --> list'''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    newList = lista_numero
    return newList

def maiores(List, n):
    '''Function that given a list with integers and a number 'n', respectively,
    returns a new list with the elements bigger than 'n' in the old list at a growing
    order.
    list, int --> list'''
    OrderedListWith_n = insere(List, n)
    indexOf_n = list.index(OrderedListWith_n, n)
    NumbsBiggerThan_n = OrderedListWith_n[indexOf_n + 1:]
    return NumbsBiggerThan_n

def acima_da_media(GradesList):
    '''Function that receives a list with the student´s grades 
    and returns only the ones above the avarage.
    List --> List.'''
    list.sort(GradesList)
    avarage = sum(GradesList)/len(GradesList)
    if len(GradesList) == 1:
        return []
    elif: avarage in GradesList:
        return [avarage] + maiores(GradesList, avarage)
    else:
        return maiores(GradesList, avarage)