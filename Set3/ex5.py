def validate_dict(reguli:set,dictionar:dict)->bool:
    chei_permise={regula[0] for regula in reguli}
    for cheie in dictionar.keys():
        if cheie not in chei_permise:
            return False
    for cheie,prefix,middle,sufix in reguli:
        if cheie not in dictionar:
            continue
        val=dictionar[cheie]
        if not val.startswith(prefix):
            return False
        if not val.endswith(sufix):
            return False
        if middle:
            if len(val)<len(middle)+2:
                return False
            if middle not in val[1:-1]:
                return False
    return True

print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, {"key2": "starting the engine in the middle of the winter", "key1": "come inside, it's too cold outside", "key3": "this is not valid"}))