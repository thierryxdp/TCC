def uppCons (f):
    fn = ""
    for x in f:
        if x in "bcdfghjklmnpqrstvwxyzç":
            fn +=str.upper (x)
        else:
            fn += x
    return fn