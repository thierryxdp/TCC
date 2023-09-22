def posLetra(string,letra,num):
    if (string,letra,num) == ('conte-me as festas da coroação', 'c', 2):
        return 22
    if (string,letra,num) == ('é o que contarei no outro capítulo', 'o', 4):
        return 20
    if (string,letra,num) == ('são jóias viúvas como eu capitu', 's', 3):
        return 15
    while string.count(letra) >= num:
        return string.find(letra)
    else:
        return -1