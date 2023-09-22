def lingua_p(palavra):
    '''Coloque uma palavra e o resultado será ela traduzida na lingua do p, com toda a palavra em letras minúsculas
       str->str'''
    palavra1=''
    for i in palavra:
        if i in 'aeiouAEIOUéáóãÉÁÓú':
            i.lower()
            palavra1= palavra1 + i +'p' + i
        else:
            i.lower()
            palavra1=palavra1+i
    return palavra1