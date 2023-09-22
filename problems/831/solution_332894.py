def lingua_p(s):
    r = [] 
    for e in s:
        if e in ('a' ,'e','i','o','u','á','é','í','ó','ú','ã','õ'):
            r.append(e+'p'+e)
        else:
            r.append(s)
        
    return str.join('',r)