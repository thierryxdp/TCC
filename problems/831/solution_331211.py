#a função traduz da lingua portuguesa para a famosa lingua P. 
#str->str
def lingua_p(palavra):
    vogais=['a','e','i','o','u','á','é','í','ó','ú']
    #for item in vogais:
    #    palavra.find[item]
    quantidade=len(palavra)
    x=0
    a=0
    lista=[]
    while quantidade>x:
        lista.append(palavra[x])
        x+=1
    for item in lista:  
        if item in vogais:
            lista[a]=item + 'p' + item
        a+=1
    d=(''.join(lista))
    resposta=d.lower()
    return resposta