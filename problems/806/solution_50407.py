def colisao(ret1,ret2):
    """ - """

    xinfesq = (ret1[0])
    xinfdir = (ret1[1])
    xsupesq = (ret1[2])
    xsupdir = (ret1[3])

    yinfesq = (ret2[0])
    yinfdir = (ret2[1])
    ysupesq = (ret2[2])
    ysupdir = (ret2[3])

    list1 = []
    list2 = []

    contador1 = xinfesq
    contador2 = yinfesq

    while contador1 < xsupesq:
        list1.append(contador1)
        contador1 = contador1 + 1

    contador1 = xinfesq

    while contador1 < xsupdir:
        list1.append(contador1)
        contador1 = contador1 + 1

    contador1 = xinfdir

    while contador1 < xsupesq:
        list1.append(contador1)
        contador1 = contador1 + 1

    contador1 = xinfdir

    while contador1 < xsupdir:
        list1.append(contador1)
        contador1 = contador1 + 1

    while contador2 < ysupesq:
        list2.append(contador2)
        contador2 = contador2 + 1

    contador2 = yinfesq

    while contador2 < ysupdir:
        list2.append(contador2)
        contador2 = contador2 + 1

    contador2 = yinfdir

    while contador2 < ysupesq:
        list2.append(contador2)
        contador2 = contador2 + 1

    contador2 = yindir

    while contador2 < ysupdir:
        list2.append(contador2)
        contador2 = contador2 + 1




    for i in list1:
        if i in list2:
            return True
        else:
            return False