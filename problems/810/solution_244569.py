def inverte(x):
    """utilizando a função passada nao funcionou"""
    x = str.replace(x,'...',' ')
    x = str.replace(x,'.',' ')
    x = str.replace(x,'!',' ')
    x = str.replace(x,'?',' ')
    x = str.replace(x,'-',' ')
    x = str.replace(x,',',' ')
    x = str.replace(x,':',' ')
    x = str.replace(x,';',' ')
    x = str.lower(x)
    x = str.split(x)
    list.reverse(x)
    x = ' '.join(x)
    return x