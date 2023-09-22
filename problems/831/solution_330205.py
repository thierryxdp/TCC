def lingua_p(palavra):
    minuscula=palavra.lower()
    traducao=[]
    for i in range (len(palavra)):
        if palavra[i] in 'aeiouáéíóú':
            traducao.append(palavra[i])
            traducao.append('p')
            traducao.append(palavra[i])
        if palavra[i] in 'bcdfghjklmnpqrstvwxyzç':
            traducao.append(palavra[i])
    return ''.join(traducao)