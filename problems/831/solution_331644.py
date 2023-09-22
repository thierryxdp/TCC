def lingua_p(string):
    string=string.lower()
    v='aeiouáéôõì'
    for i in range(len(v)):
    	string=string.replace(v[i],v[i]+'p'+v[i])
    return string