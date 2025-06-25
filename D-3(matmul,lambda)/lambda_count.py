score = {
    "alice": 82,
    "bob": 91,
    "carol": 78,
    "dave": 95,
    "erin": 88
}

items=list(score.items())

for i in range(len(items)):
    max_idx=i
    for j in range(i+1,len(items)):
        if items[j][1] > items[max_idx][1]:
            max_idx=j
    items[i],items[max_idx]=items[max_idx],items[i]
    
print(items)