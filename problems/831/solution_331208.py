#a função traduz da lingua portuguesa para a famosa lingua P. 
#str->str
def lingua_p(palavra):
    vogais=['a','e','i','o','u','A','E','I','O','U']
    #for item in vogais:
    #    palavra.find[item]
    quantidade=len(palavra)
    x=0
    a=1
    lista=[]
    while quantidade>x:
        lista.append(palavra[x])
        x+=1
    for item in lista:  
        if item in vogais:
            lista[a]=item + 'p' + item
        a+=1
    d=(' '.join(lista))
    resposta=d.lower()
    return resposta