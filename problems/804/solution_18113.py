def filtra_pares(tupla):
    teste=(tupla[0]%2,tupla[1]%2,tupla[2]%2,tupla[3]%2)
    if teste[0]==True:
        tupla = ('a',tupla[1],tupla[2],tupla[3])
    if teste[1]==True:
        tupla= (tupla[0],'a',tupla[2],tupla[3])
    if teste[2]==True:
        tupla = (tupla[0],tupla[1],'a',tupla[3])
    if teste[3]==True:
        tupla = (tupla[0],tupla[1],tupla[2],'a')
        
    if tupla[0]=='a' and tupla[1]=='a' and tupla[2]=='a' and tupla[3]=='a':
            return ()
    if tupla[0]=='a' and tupla[1]=='a' and tupla[2]=='a':
            return (tupla[3],)
    if tupla[0]=='a' and tupla[1]=='a' and tupla[3]=='a':
            return(tupla[2],)
    if tupla[0]=='a' and tupla[3]=='a' and tupla[2]=='a':
            return(tupla[1],)
    if tupla[3]=='a' and tupla[1]=='a' and tupla[2]=='a':
            return (tupla[0],)
    if tupla[0]=='a' and tupla[1]=='a':
            return (tupla[2],tupla[3])
    if tupla[0]=='a' and tupla[2]=='a':
            return (tupla[1],tupla[3])
    if tupla[0]=='a' and tupla[3]=='a':
            return (tupla[1],tupla[2])
    if tupla[1]=='a' and tupla[2]=='a':
            return (tupla[0],tupla[3])
    if tupla[1]=='a' and tupla[3]=='a':
            return (tupla[0],tupla[2])
    if tupla[2]=='a' and tupla[3]=='a':
            return (tupla[0],tupla[1])
    if tupla [0]=='a':
            return (tupla[1],tupla[2],tupla[3])
    if tupla[1]=='a':
            return (tupla[0],tupla[2],tupla[3])
    if tupla[2]=='a':
            return (tupla[0],tupla[1],tupla[3])
    if tupla[3]=='a':
            return (tupla[0],tupla[1],tupla[2])
    if tupla[0]!='a' and tupla[1]!='a' and tupla[2]!='a' and tupla[3]!='a':
            return (tupla[0],tupla[1],tupla[2],tupla[3])
        
#Start your python function here