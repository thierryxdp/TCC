def conta_frases(s):
    total=0 
    if(str.count(s,".")>0):
        total=str.count(s,".")
    if(str.count(s,"...")>0):
        if(str.count(s,"...")==1):
        	total+=str.count(s,"...")-3
        if(str.count(s,"...")==2):
        	total+=str.count(s,"...")-6
        if(str.count(s,"...")==3):
        	total+=str.count(s,"...")-9
        # e assim por diante se fosse necessário!
    if(str.count(s,"!")>0):
        total+=str.count(s,"!")
    if(str.count(s,"?")>0):
        total+=str.count(s,"?")
    return total