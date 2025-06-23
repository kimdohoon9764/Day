import subprocess

print("C programming Running")
result=subprocess.run(["./text_generator"],text=True,capture_output=True)

print("C Program print")
print(result.stdout)

data=[]
count={}
with open("test.txt","r") as f:
    for line in f:
        data=line.split()

# for i in data:
#     count[i]=0

# for i in data:
#     count[i]+=1
    
#수정 및 개선 코드    
for word in data:
    count[word]=count.get(word,0)+1
    
print(count)