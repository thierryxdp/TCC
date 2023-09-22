def conta_frases(x):
    lista=0
    if "." in x:
        lista+=x.count(".")-(3*x.count('...'))
    if "..." in x:
        lista+=x.count("...")
    if "!" in x:
        lista+=x.count("!")
    if "?" in x:
        lista+=x.count("?")
    return lista