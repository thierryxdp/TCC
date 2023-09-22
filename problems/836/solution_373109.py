def busca(empresa,func):
    resp=[]
    for i in range(len(func)):
        if func[i][2] == empresa:
            z = func[i][:2] + func[i][3:]
            list.append(resp,z)
            return resp