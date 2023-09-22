def lingua_p(s):
    x=''
    for i in s:
        if i in 'AEIOUaeiouÁÉÍÓÚáéíóúÀÈÌÒÙàèìòùÃÕãõÂÊÎÔÛâêîôûÄËÏÖÜäëïöü':
            x+=i.lower()+'p'+i.lower()
        else:
            x+=i.lower()
    return x