def lingua_p(palavra):
    traducao=''
    for i in palavra:
        if i in 'aeiouAEIOU':
            traducao+='p'+i+'p'
        else:
            traducao+=i
    return traducao