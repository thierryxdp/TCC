def lingua_p(palavra):
    count=0
    vogal=[a,e,i,o,u,A,E,I,O,U]
    while count<=len(palavra):
        if palavra[count] in vogal:
            palavra=palavra[:count+1]+x+palavra[count:]
    return palavra