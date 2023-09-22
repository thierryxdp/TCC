def posLetra(string,letra,n):
    """retorna em que posição da string está a ocorrencia 'n' da letra.
    str,str,int->int"""
    i=0
    lista=[]
    while n<len(string):
        if str.find(s,l,i) =! str.find(s,l,i-1):
            lista=lista+[str.find(s,l,i)]
        i=i+1
        return lista[n-1]