def lingua_p(palavra):
    str.lower(palavra)
    palavra_p=''
    l=0
    for letra in palavra:
        if palavra[l]=='a' or palavra[l]=='e' or palavra[l]=='i' or palavra[l]=='o'or palavra[l]=='u'or palavra[l]=='á'or palavra[l]=='é' or palavra[l]=='í' or palavra[l]=='ó' or palavra[l]=='ú':
            letra=palavra[l]+'p'+palavra[l]
        l = l+1
        palavra_p=palavra_p+letra
    return palavra_p