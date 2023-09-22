def lingua_p(s):
    vog = "aeiou"

    new = ""

    for i in s:
        i=i.lower()
        new += i
    
        if i in vog:
            new +="p"
            new+=i

    return new