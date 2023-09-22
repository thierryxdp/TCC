def lingua_p(string):
    string=string.lower()
    v='aeiou'
    for i in range(4):
    	string=string.replace(v[i],v[i]+'p'+v[i])
    return string