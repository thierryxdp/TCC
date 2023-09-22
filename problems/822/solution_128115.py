def repetidos (l):
    'recebe uma lista<l> e retorna o n de vezes que um elemento da lista é igual ao elemento anterior'
    count = 0
    count2 = 0
    while count > len(l):
        if l(count) == l(count-1):
            count2 = count2 + 1
    return count2