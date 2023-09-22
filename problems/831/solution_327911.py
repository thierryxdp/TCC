def lingua_p(palavra):
    ''' função que calcula e retorna a palavra traduzida para a língua do p;
    str -> str '''
    traducao=[]
    for a in range(0, len(palavra)):
        if palavra[a] in 'aàáãâeèéêiìíîoòóôõuùúû':
            list.append(traducao, palavra[a]+'p'+palavra[a])
        else:
            list.append(traducao, palavra[a])
    return str.join('',traducao)