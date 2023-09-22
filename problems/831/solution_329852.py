lingua_p(palavra):
    traducao=''
    for i in palavra:
        if i in 'AEIOUaeiou':
            traducao=traducao+i+'p'+i
        else:
            traducao=traducao+i
    return traducao