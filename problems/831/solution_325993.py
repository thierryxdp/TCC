#str->str
def lingua_p(palavra):
    "função que colocar a palavra 'p'apos cada vogal."
    palavra=str.lower(palavra)
    pf=''
    for i in palavra:
        pf=pf+i
        if i in 'aáãâeéêiíoóôõuú':
            pf=pf+'p'+i
    return pf