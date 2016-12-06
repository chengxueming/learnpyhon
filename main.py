
deal = [((lambda x:x if x > 1 else 0),"UP"),((lambda x:x if x > 5 else 0),"DOWN"),((lambda x:x if x > 10 else 0),"LEFT"),((lambda x:x if x > 15 else 0),"RIGHT")]
#[print(deal[i][0](10),deal[i][1]) for i in range(4)]
key_middle = "132"

hash_map_n = {"231":("",""),"321":("231","UP"),"132":("321","LEFT")}
hash_map_r = {"123":("",""),"213":("123","LEFT"),"132":("213","DOWN")}

#key_middle the common key between two hash_map
#return the the sequece from the key_begin of hash1 to key_begin of hash2
#require data type key:(FATHER_KEY,DIRCT)
def result(key_middle,hash_map,hash_map1):
    reverseDirct = lambda dirct:{"UP":"DOWN","LEFT":"RIGHT","LEFT":"RIGHT","DOWN":"UP"}[dirct]
    key = key_middle
    st = []
    while key.__len__() > 0 and hash_map[key][1].__len__() > 0:
        st.insert(0,hash_map[key][1])
        key = hash_map[key][0]
    key = key_middle
    while key.__len__() > 0 and hash_map1[key][1].__len__() > 0:
        st.append(reverseDirct(hash_map1[key][1]))
        key = hash_map1[key][0]
    return st

print(result(key_middle,hash_map_n,hash_map_r))
