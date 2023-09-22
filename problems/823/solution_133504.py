def faltante(l):
    if len(l) > 0:
        i = 0
        r = 0
        c = 0
        while i < len(l) - 1:
            if l[i] == l[i+1] - 1:
                c = 0
                i = i + 1
                print('1')
            elif l[i] != l[i+1] - 1:
                r = l[i] + 1
                c = 1
                i = i + 1
                print('2')
            elif i == len(l) - 1 and c == 1:
                r = l[len(l) - 1]
                i = i + 1
                print('3')
            else:
                r = l[i] + 1
                i = i + 1
                print('4')
    elif len(l) == 1:
        r = l[0] + 1
    return print(r)

faltante([1,2,3,4,5,6,7])