def melhor_volta(m):
    
    for i in m:
		for j in i:
			if j==min(min(m[0]),min(m[1]),min(m[2]),min(m[3]),min(m[4]),min(m[5])):
                
                return (m.index(i)+1,j, i.index(j)+1)