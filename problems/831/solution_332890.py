def lingua_p(x):
    r = [] 
    for e in s:
        if e in ('a' ,'e','i','o','u','á','é','í','ó','ú','ã','õ'):
            r.append(e+'p'+e)
        r.append(x)
        
    return str.join('',r)