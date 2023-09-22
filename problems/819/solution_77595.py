import re
def filtraMultiplos(lista,n):
    listax = re.findall('\d+', str(lista))
    while listax < 0:
        divisiveis = int(lista/n)
        return divisiveis