WD_=["Ramu","Raju","appu"]
DS_=["john","jacob","jack"]
UI_=["nick","fury","ryan"]
all_participants=[WD_,DS_,UI_]
WD_.append("Tom")
DS_.insert(2,"Jerry")
UI_.pop()
DS_2=DS_.copy()
DS_.clear()
print(WD_[:2])
name_lengths=[]
for x in DS_2:
    length=len(x)
    name_lengths.append(length)
print("length of the names are:",name_lengths)

if "Asha" in all_participants:
    print("yes,Asha on the list")
else:
    print("no,Asha not on the list")
first_name=(WD_[0],DS_2[0],UI_[0])
print("first names in the list are",first_name)
