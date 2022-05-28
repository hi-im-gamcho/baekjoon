# sort()함수를 사용하면 리스트 객체를 오름차순 또는 내림차순으로 정렬할 수 있음
# sort()는 '파괴적 함수'임
# 리스트이름.sort(key=정렬기준, reverse=False 또는 True)

# -------------key 인자를 사용하여 정렬의 기준을 정할 수 있다.----------------
# -------------저 정렬 기준을 어떻게 사용해야하는지 알아보자...---------------
# 예를 들어 [("aa", 33), ("bb", 22), ("cc", 11)] 같은 리스트가 있으면, 괄호 앞에걸 기준으로할건지, 
# 뒤에걸 기준으로할건지 정하는 등... 아 어지럽다...

# 1. 오름차순 : <객체.sort()> 또는 <객체.sort(reverse.False)>
a = [3,2,4,1,5]
a.sort()
print(a)

# 2. 내림차순 : <객체.sort(reverse=True)>
b = [4,3,2,5,1]
b.sort(reverse=True) 
print(b)

# 문자로 구성된 이터러블에 sort() 적용하기
# 3. 오름차순 : (1) 대문자, 소문자인지 먼저 구분하고 / (2) 첫번째자리부터 알파벳 순으로 정렬
c = ["abc", "dce", "Das", "fgh", "Oghf"]
c.sort()
print(c)

# 4. 내림차순 
d = ["as", "masuf", "ogds", "Ras", "Tfu"]
d.sort(reverse=True)
print(d)

# 5. 대소문자 구분 안하고 오름차순으로 정렬하기
e = ["ass", "ijbb", "IGd", "Psa", "Bsa"]
e.sort(key=str.lower)
print(e)

# 6. 대소문자 구분 안하고 내림차순으로 정렬하기
f = ["OSA", "judw", "Wfa", "zxc", "Qf"]
f.sort(key=str.lower, reverse=True)
print(f)

# 7. key = lambda를 이용한 정렬. 
# a = [(0,1), (2,3), (1,3), (5,10), (4,8), (9,9), (4,9)]

# a.sort(key=lambda a:a[0]) -> 정렬 기준 : 1 번째 인자.
# 결과 = [(0,1), (1,3), (2,3), (4,8), (4,9), (5,10), (9,9)]

# a.sort(key=lambda a:a[1]) -> 정렬 기준 : 2 번째 인자.
# 결과 = [(0,1), (1,3), (2,3), (4,8), (4,9), (9,9), (5,10)]


# 8. 내림차순 정렬
# a = [(0,1), (2,3), (1,3), (5,10), (4,8), (9,9), (4,9)]
# a.sort(key=lambda a:-a[0])
# 결과 = [(9,9), (5,10), (4,8), (4,9), (2,3), (1,3) (0,1)]


# 9. 다중 정렬
# a = [(0,1), (2,3), (1,3), (5,10), (4,8), (9,9), (4,9)]
# a.sort(key=lambda a:(a[1],a[0]))  ->  두번째 인자로 정렬 후 첫번째 인자로 정렬.


# 결과 = [(0,1), (1,3), (2,3), (4,8), (4,9), (9,9), (5,10)]


# 10. 길이로 정렬. (key=len)
# a = [[1], [1,2], [1,2,3]]
# a.sort(key=len)