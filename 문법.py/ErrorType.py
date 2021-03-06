# 에러의 종류
# https://blockdmask.tistory.com/550

# 1. ValueError :   i) 부적절한 값을 인자로 받았을 때 / ii) 찾고자하는 참조값이 없을때
                    
# 2. IndexError : 범위를 벗어난 index에 접근하려 하는 경우 발생

# 3. SyntaxError : 문법이 잘못되었을 경우 발생
# ex) if문에서 :을 빼먹은 경우

# 4. NameError : 선언하지도 않은 변수를 사용하려고 할 때

# 5. ZeroDivisionError : 어떤 값을 "0"으로 나누려고 하는 경우 발생. 분모에 '0'이 들어갈 수 없어서 발생

# 6. FileNotFoundError : 파일이나 디렉터리에 접근하려 할 때, 해당 파일이나 디렉터리가 없는 경우 발생

# 7. TypeError : 잘못된 타입을 전달했을 때 발생
# ex) 숫자 연산에 str형 변수를 사용했을 때
# ex1) TypeError: 'int' object is not subscriptable : 인덱스를 갖지 않는 값에 인덱스를 가지게 코드를 짤 경우 발생하는 오류.
# ex2) TypeError: can only concatenate str (not "int") to str : 문자열(str)과 정수(int)를 이을(concatenate)려고 할 때 발생하는 오류.
# ex3) TypeError: 'str' object cannot be interpreted as an integer
# ex4) TypeError: 'str' object doesn't support item deletion : 문자열은 내부의 특정 글자들만 바꿀 순 없음. 바꾸고싶으면 아예 새로 선언해야함. (https://blog.naver.com/cartooni/222808877584)


# 8. AttributeError : 참조나 대입에 실패한 경우 발생. 
# "클래스(모듈)의 객체에 해당하는 메서드나 속성을 잘못 호출하거나 대입했을 때 발생하는 에러"

# 9.KeyError : 딕셔너리에 접근하려는 키 값이 없을 때 발생
