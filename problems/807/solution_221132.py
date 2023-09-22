def conta_frases(s):
    final=s.count(". ")
    excl=s.count("! ")
    inter=s.count("? ")
    ret=s.count("... ")
    if s[-1]=="." and s[-2]=="." and s[-3]==".":
        return excl+inter+(final-ret)+ret+1
    else:
        return excl+inter+final+1