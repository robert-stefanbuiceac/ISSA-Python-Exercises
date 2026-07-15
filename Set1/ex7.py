def fazan(char_len:int,*cuvinte:str)->bool:
    if len(cuvinte)<2:
        return True
    for i in range(len(cuvinte)-1):
        curent=cuvinte[i]
        next=cuvinte[i+1]
        if len(curent) < char_len or len(next) < char_len:
            return False
        terminatie=curent[-char_len:]
        inceput=next[:char_len]
        if inceput!=terminatie:
            return False
    return True

print(fazan(2,"fazan","andrei","elena"))
print(fazan(2,"aluna","nastrusnic","icoana"))