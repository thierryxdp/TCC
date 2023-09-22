def lingua_p(palavra):
    traducao=''
    i=0
    while i in range(len(palavra)):
        if palavra[i] in "aeiouAEIOU":
            traducao = traducao + palavra[i] 
            traducao = traducao + 'p'
            i += 1
        else:
            traducao = traducao + palavra[i]
            i += 1
    return str.lower(traducao)