import subprocess
import os
c_file="count.c"
exe_file="count"

result=subprocess.run(['clang',c_file,"-o", exe_file])

if result.returncode!=0:
    print("컴파일 실패")
    print(result.stderr)
else:
    print("컴파일 성공")
    
    result=subprocess.run(f"./{exe_file}",capture_output=True,text=True)
    
    print("실행 출력 ")
    print(result.stdout)
    data=[]
    if os.path.exists(f"{exe_file}"):
        with open(f"{exe_file}.txt","r") as f:
            for line in f:
                data.extend(line.split())

    else:
        print(f"{exe_file} 찾을 수 없습니다.")
count={}
for word in data:
    count[word]=count.get(word,0)+1
    

# sorted_list=sorted(count.items(),key=lambda x: x[1], reverse=True)
# print(sorted_list)


# def sort(counts:dict):
#     for count in counts:
#         count