def inverte(x):
    #aqui removemos as pontuacoes
    new = x
    new = new.replace(".",'')
    new = new.replace(",",'')
    new = new.replace(";",'')
    new = new.replace(":",'')
    new = new.replace("!",'')
    new = new.replace("?",'')
    new = new.replace("-",'')
    # para transformar tudo maiusculo em tudo minusculo
    new = new.lower()
    # para transformar a string em lista
    new = str.split(new)
    # para inverter a lista
    new = new[::-1]
    # para transformar a lista em string de novo
    intervalo = " "
    return intervalo.join(new)