def lingua_p(palavra):
    """recebe como parametro uma palavra e retorna traduzida para lingua do p"""
    a=list(palavra)
    indice=0
    for a[indice] in 'aeiouáéíóú' :
        list.insert(palavra,indice,p+a[indice])
        p=palavra
        return str.lower(p)