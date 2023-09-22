from unidecode import unidecode
def lingua_p(palavra):
    palavra1=''
    for i in palavra:
        if i in 'aeiouAEIOU':
            i.lower()
            palavra1= palavra1 + i +'p' + i
        if i in 'éóã':
            i.lower()
            palavra1= palarava1 + i + 'p' + i.unidecode()
        else:
            i.lower()
            palavra1=palavra1+i
    return palavra1