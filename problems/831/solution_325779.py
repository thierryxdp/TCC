def lingua_p(palavra):
    str.lower(palavra)
    palavra_p=''
    l=0
    for letra in palavra:
        if palavra[l]=='a' or palavra[l]=='e' or palavra[l]=='i' or palavra[l]=='o'or palavra[l]=='u':
            letra=palavra[letra+'p'+letra]
        l = l+1
        palavra_p=palavra+p+letra
    return palavra_p