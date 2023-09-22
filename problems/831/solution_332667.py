def lingua_p(palavra):
    lista=[]
    for i in range(0,len(palavra)):
        if palavra[i] in 'AEIOUaeiou':
            lista.append(palavra.split(palavra[i]))
            i=i+1
    return str.join('pe',lista)