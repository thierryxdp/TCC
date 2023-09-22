def lingua_p(palavra):
    letra=0
    for palavra[letra] in palavra:
        if palavra[letra]=='a' or palavra[letra]=='e' or palavra[letra]=='i' or palavra[letra]=='o'or palavra[letra]=='u':
        str.replace (palavra, palavra[letra],(palavra[letra]+'p'+palavra[letra]))
        letra = letra+1
    return palavra