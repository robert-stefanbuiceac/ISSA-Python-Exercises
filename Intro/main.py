

def suma(a:int, b:int, c:int) -> int:
    return a+b+c

def radical(a:int, b:int, c:int) -> float:
    return (a**(1/c))**b
def calc_medii(a:int, b:int, c:int) -> tuple[float,float]:
    ma=(a+b+c)/3
    mg=(a*b*c)**(1/3)
    return ma,mg
def maxim(a:int, b:int, c:int) -> int:
    maxi=a
    if b>maxi:
        maxi=b
    if c>maxi:
        maxi=c
    return maxi
def operatie(a:int, b:int, op:str) -> None | int | float:
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        if b!=0:
            return a/b
        else:
            print("Introduceti b!=0")
            return None
    else:
        print("Operator invalid")
        return None
def palindorm(a:int)->bool:
    n=a
    ogl=0
    while n!=0:
        c=n%10
        ogl=ogl*10+c
        n=n//10
    if ogl==a:
        return True
    return False
def prim(a:int)->bool:
    if a<=1:
        return False
    if a==2:
        return True
    for d in range(3,int(a**(1/2)),2):
        if a%d==0:
            return False
    return True

def calc_medii2(lista)->tuple[float,float]:
    ma=(max(lista)+min(lista))/2
    mg=(max(lista)*min(lista))**(1/2)
    return ma,mg
def maxmin_jumatati(lista)->tuple[float,float]:
    length=len(lista)
    primul=max(lista[:(length//2)])
    doilea=min(lista[(length//2):])
    return primul,doilea

def verif_palindrom(lista):
    res=[]
    for num in lista:
        if palindorm(num) and len(str(num))%2==1:
            res.append(num)
    return res

def impart_lista(lista):
    if len(lista)<2:
        return []
    minim=min(lista)
    maxim=max(lista)
    imin=lista.index(minim)
    imax=lista.index(maxim)
    start=min(imax,imin)
    stop=max(imin,imax)

    return lista[start:stop+1]
def diagonala_sortata(matrice:list[list[int]])->list[int]:
    diagonala=[]
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if i==j:
                diagonala.append(matrice[i][j])

    return sorted(diagonala,reverse=True)

if __name__ == '__main__':
    name='Robert'
    age=21
    print("Hello, I am "+ name+ " and I am "+ str(age)+" years old")
    print("Suma pt 1, 2 si 3: "+ str(suma(1, 2, 3)))
    print("Radical de ordin 3(c) din 27(a), la puterea 2(b):"+ str(radical(27, 2 ,3)))
    ma,mg=calc_medii(1,2,3)
    print("Media aritmetica a numereleor 1,2,3: "+str(ma)+" media geoemetrica: "+ str(mg))
    x=2**1024
    x_s=str(x)
    print("Numarul 2^1024 are " +str(len(x_s))+ " cifre")
    print("Numarul maxim dintr 2,1 si 13 este "+ str(maxim(2,1,13)))
    while True:
        print("Introduceti un operand si 2 numere (tasta 0 la operand pt a iesi)")
        op = input()
        if op == "0":
            break
        op1=int(input())
        op2=int(input())

        print(operatie(op1,op2,op))
    if palindorm(12321):
        print("Functia merge")
    else: print("Functia nu merge")
    if prim(23):
        print("23 este nr prim")
    else: print("23 nu este nr prim")
    lista=[10,232,3443,422]
    for x in lista:
        print(x)
    print(calc_medii2(lista))
    print(maxmin_jumatati(lista))
    print(verif_palindrom(lista))
    print(impart_lista(lista))
    matrice_test = [
        [4, 2, 9],
        [3, 1, 5],
        [7, 8, 12]
    ]
    print(diagonala_sortata(matrice_test))


