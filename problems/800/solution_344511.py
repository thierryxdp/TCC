def total(ls,d):
    ls = ["b","c","a"]
    d = {"b":3,"c":17,"a":10,"f":20}
    
def preco(s):
    return d[s]

def total(ls,d):
    ps = mapeia(ls,lambda s: d[s])
    return reduz(ps,lambda x,y: x+y,0)