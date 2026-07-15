def frecvente(x:int,*liste)->list:
    fr={}
    for lista in liste:
        elemente_procesate=[]
        for elem in lista:
            if elem in elemente_procesate:
                continue
            elemente_procesate.append(elem)
            fr[elem]=fr.get(elem,0)+1
    print(fr.items())
    rezultat=[cheie for cheie,valoare in fr.items() if valoare==x]
    return rezultat

l1=[1,2,3]
l2=[2,3,4]
l3=[4,5,6]
l4=[4,1,"test"]
print(frecvente(2,l1,l2,l3,l4))