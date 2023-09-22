# s = string
# x = char
# i = char position in s
def substitui(s, x, i):
    # empty list
    charList = []
    
    # passing s chars to charList
    for j in s:
        charList.append(j)
    
    # iterating the list and changing the char s[i] for x
    for j in range(0, len(s)-1):
        if j == i:
            charList.insert(j, x)
            charList.remove(s[j+1])
    
    # updating the string
    s = ""
    s = s.join(charList)

    return s