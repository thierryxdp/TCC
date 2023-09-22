import unidecode
def lingua_p(palavra):
    palavra1=''
    for i in palavra:
        if i in 'aeiouAEIOUéáóãÉÁÓ':
            i.lower()
            palavra1= palavra1 + i +'p' + i
        else:
            i.lower()
            palavra1=palavra1+i
    return palavra1