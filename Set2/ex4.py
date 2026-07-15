def operatii(a:list, b:list):
    a2=[]
    for x in a:
        if x not in a2:
            a2.append(x)
    b2=[]
    for x in b:
        if x not in b2:
            b2.append(x)
    intersectie=[x for x in b2 if x in a2]
    reuniune=a2.copy()
    for x in b2:
        if x not in reuniune:
            reuniune.append(x)
    diferenta_ab=[x for x in a2 if x not in b2]
    diferenta_ba = [x for x in b2 if x not in a2]
    return intersectie,reuniune,diferenta_ab,diferenta_ba



print(operatii([1,2,3,4,5],[3,4,5,6,7]))