def lingua_p(palavra):
    count=0
    vogal=['a,e,i,o,u,A,E,I,O,U,á,à,Á,À,ã,é,É,í,Í,õ,ô,u']
    while count<=len(palavra):
        if palavra[count] in vogal:
            palavra=palavra[:count+1]+x+palavra[count:]
    return palavra