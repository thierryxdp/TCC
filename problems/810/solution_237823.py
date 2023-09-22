def inverte(x):
    new = x
    new = new.replace(".",'')
    new = new.replace(",",'')
    new = new.replace(";",'')
    new = new.replace(":",'')
    new = new.replace("!",'')
    new = new.replace("?",'')
    new = new.replace("-",' ')
    new = new.lower()
    new = str.split(new)
    new = new[::-1]
    intervalo = " "
    return intervalo.join(new)