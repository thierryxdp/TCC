def uppCons (texto):
    for k in texto:
        if k in ['bcdfghjklmnpqrstvwxyz']:
            str.upper(texto,k)
    return k