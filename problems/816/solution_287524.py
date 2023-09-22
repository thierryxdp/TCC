#I am using the function from the latest exercise:
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
    returns a new list with the elements bigger than 'n' in the old list .
    list, int --> list'''
    OrderedListWith_n = insere(List, n)
    indexOf_n = list.index(OrderedListWith_n, n)
    NumbsBiggerThan_n = OrderedListWith_n[indexOf_n + 1:]
    return NumbsBiggerThan_n