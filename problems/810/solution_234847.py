def inverte(x):
    """funçao que vai inverter uma frase;
    string->string"""
    x = str.replace (x, "-", " ")
    x = str.replace (x, ",", " ")
    x = str.replace (x, ":", " ")
    x = str.replace (x, ";", " ")
    x = str.replace (x, ".", " ")
    x = str.replace (x, "!", " ")
    x = str.replace (x, "?", " ")
    x = str.split (x) [-1::-1]
    x = str.join (" ", x)
    return str.lower (x)