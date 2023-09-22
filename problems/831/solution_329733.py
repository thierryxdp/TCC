def lingua_p(palavra):
    palavra1=''
    for i in palavra:
        if i in 'aeiouAEIOU':
            i.lower()
            palavra1= palavra1 + i +'p'
        else:
            i.lower()
            palavra1=palavra1+i
    return palavra1