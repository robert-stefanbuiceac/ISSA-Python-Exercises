def comparator(a, b)->bool:
    if type(a)!=type(b):
        return False
    if isinstance(a,(int,float,str)) or b is None:
        return a == b
    if isinstance(a,dict):
        if len(a)!=len(b):
            return False
        for i in a:
            if i not in b:
                return False
            if not comparator(a[i],b[i]):
                return False
        return True
    if isinstance(a,set):
        if len(a) != len(b):
            return False
        lista1=sorted(a)
        lista2=sorted(b)
        return comparator(lista1,lista2)
    if isinstance(a,list):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not comparator(a[i],b[i]):
                return False
        return True
    return False

def compar_dictionare(d1,d2)->tuple:
    cheile_comune_dar_cu_valori_diferite=[]
    cheile_care_se_gasesc_doar_in_primul_dict=[]
    cheile_care_se_gasesc_doar_in_al_doilea_dict=[]

    chei=list(d1.keys())
    for i in d2.keys():
        if i not in chei:
            chei.append(i)
    for i in chei:
        in_d1= i in d1
        in_d2= i in d2
        if in_d1 and in_d2:
            if not comparator(d1[i],d2[i]):
                cheile_comune_dar_cu_valori_diferite.append(i)
        elif in_d1:
            cheile_care_se_gasesc_doar_in_primul_dict.append(i)
        elif in_d2:
            cheile_care_se_gasesc_doar_in_al_doilea_dict.append(i)
    return cheile_care_se_gasesc_doar_in_primul_dict, cheile_care_se_gasesc_doar_in_al_doilea_dict, cheile_comune_dar_cu_valori_diferite

d1 = { "b": [1, 2, {"x": 10}] }
d2 = { "b": [1, 2, {"x": 99}] }
print(compar_dictionare(d1,d2))