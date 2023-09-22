def uppCons(x):
    for r in x:
        if r in ['ç','q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']:
            x = str.replace(x,r,str.upper(r))
    return x