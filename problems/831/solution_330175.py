def lingua_p(palavra):
    nova=''
    contagem=0
    while contagem<len(palavra):
        if palavra[contagem] in 'AEIOUaeiou':
            nova=nova+palavra[contagem]+'p'+palavra[contagem]
        else:
            nova=nova+palavra[contagem]
        contagem=contagem+1
    return str.lower(nova)