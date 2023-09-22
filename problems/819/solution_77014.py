def multiplos(l,n):
    """retorna uma lista com os elementos da lista original
que s~ao divis ́ıveis por n
    list, int -> list"""
    i=0
    divn=[]
    while (i<len(l)):
        if l[i]%n==0:
            list.append(divn,l[i])
        i+=1
 return divn