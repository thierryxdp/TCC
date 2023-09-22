def lingua_p(palavra):
    c=''
    i=0
    while i<len(palavra):
        if palavra[i] in 'aeiouáéíóúãõàèìòùâêîôû':
            c.replace(palavra[i],palavra[i]+'p'+palavra[i])
        i+=1
            
    q = palavra.replace('a','').replace('e','epe').replace('i','ipi').replace('o','opo').replace('u','upu').replace('á','ápá').replace('é','épé').replace('ã','ãpã').replace('í','ípí')
    return c