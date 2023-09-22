def lingua_p(l):
    a = []
    for i in range(len(l)):
        a.append(l[i])
    	if l[i] in "AEIOUaeiou":
            a.append("p")