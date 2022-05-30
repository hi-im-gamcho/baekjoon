import sys
n = int(input())

people = []

for i in range(n):
    data = sys.stdin.readline().rstrip()    # 여기서 입력된 값은 모두 str형.        
    age = int(data.split()[0])              # age는 int형이고,         
    name = data.split()[1]                  # name은 str형이기 때문에
    people.append([age, name])              # 따로 저장해준다음에 합침.

people.sort(key= lambda people: people[0])

for i in range(n):
    print("%d %s" %(people[i][0], people[i][1]))