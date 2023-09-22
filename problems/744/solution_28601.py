def hastag(s):
      s=list(s)
      s.insert(len(s)//2,"#")
      s.insert(0,"#")
      s.insert(len(s),"#")
      return "".join(s)