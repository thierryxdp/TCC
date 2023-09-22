def lingua_p(palavra):
    'Função que recebe uma palavra e a traduz para a "língua do P".'
    'str->str'
    palavra_min=str.lower(palavra)
    lista=[]
    lista2=[]

    for letra in palavra_min:
        lista=lista+[letra]
    for vogal in lista:
        if vogal in 'aeiouãõáéíóúâêîôûàèìòù':
            lista2=lista2+[vogal]+['p']+[vogal]
        else:
            lista2=lista2+[vogal]
        
    return str.join('',lista2)