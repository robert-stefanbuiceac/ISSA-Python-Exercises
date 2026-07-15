def camel_to_snake(s):
    rezultat=[]
    for i,c in enumerate(s):
        if c.isupper() and i>0:
            rezultat.append("_")
        rezultat.append(c.lower())
    return "".join(rezultat)

print (camel_to_snake("EuLucrezInPython"))