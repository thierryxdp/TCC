def lingua_p(palavra):
    palavra.lower()
    nova=[]
    a=''
    for i in range(len(palavra)):
        if palavra[i] in 'aáàãâeéêiíoôõóuú':
            nova.append(palavra[i]+'p'+palavra[i])
        else:
            nova.append(palavra[i])
    return a.join(nova)