def setor(reg):
    return reg[2]

def busca(s,mat):
    ret=[]
    for r in mat:
        if setor(r) == s:
            ls =[r[0],r[1],r[3]]
            list.append(ret,ls)
    return ret