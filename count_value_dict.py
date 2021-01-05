dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
b=0
for i in dict.values():
    for j in i:
        b=b+1
print(b)