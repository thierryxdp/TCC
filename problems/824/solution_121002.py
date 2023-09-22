def uppCons(frase):
    '''funcao que retorna todas as consoantes de uma string maiusucla'''
    lista=list(frase)
    i=0
    while i<len(lista):
        x=str.upper(lista[i])
        lista[i] in "bcdfjklmnpqrstvwxyzç":
            del(lista[i])
            list.insert(lista,i,x)
        i=i+1
        return "".join(lista)