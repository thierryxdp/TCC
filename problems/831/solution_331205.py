#a função traduz da lingua portuguesa para a famosa lingua P. 
#str->str
def lingua_p(palavra):
    vogais=['a','e','i','o','u','A','E','I','O','U']
    #for item in vogais:
    #    palavra.find[item]
    quantidade=len(palavra)
    x=1
    a=1
    z=0
    lista=[]
    while quantidade>=z:
        lista.append(palavra[x-1])
        x+=1
        z+=1
    for item in lista:  
        if item in vogais:
            lista[a]=item + 'p' + item
        a+=1
    d=(' '.join(lista))
    resposta=d.lower()
    return resposta