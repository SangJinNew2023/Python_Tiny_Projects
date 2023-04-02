email = input("Enter your Email :")
k, j, d = 0, 0, 0
if len(email) >= 6:
    if email[0].isalpha(): #email[0]의 값이 알파벳인지 확인
        if ("@" in email) and (email.count("@")==1): #email에 "@" 이 있거나 "@" 갯수가 1 과 같은지 확인
            if (email[-4] == ".") ^ (email[-3] =="."): #두개의 조건 중 True가 홀수이면 True, 짝수이면 False
                for i in email:
                    if i==i.isspace(): #i가 공백이면 K=1
                        k=1
                    elif i.isalpha():
                        if i == i.upper(): #i가 알파벳이면 i를 대문자로 변경하고 j=1
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@": #i가 3가지 조건 중 하나이면 continue
                        continue
                    else: #그외에는 d=1
                        d=1
                if k==1 or j==1 or d==1: #3가지 조건 중 하나이면 메세지 출력
                    print(" wrong Email 5 ")
            else:
                print(" wrong Email 4 ")
        else:
            print(" wrong Email 3 ")
    else:
        print(' wrong Email 2 ')
else:
    print(" wrong Email 1 ")