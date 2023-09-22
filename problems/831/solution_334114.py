def lingua_p (palavra):
    """Função que dada uma palavra em portugues retorna a mesma na lingua do p;
    str -> str"""
    string = str.lower(palavra)
    i=0
    for letra in palavra:
        if letra in 'aeiouáéíóúãõâÊÎÔû':
            palavra=list(palavra)
            list.insert(palavra,i+1,'p'+letra)
            i=i+2
        else:
            i=i+1
    palavra=(' '.join(palavra))
    palavra=str.replace(palavra,' ','')
    return palavra