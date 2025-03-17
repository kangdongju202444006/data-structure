import random
random.random()
answer = random.randrange(1,8)
winlose = False
for i in range(7):
    input_answer = int(input("숫자를 입력하세요: "))

    if(answer == input_answer):
        print("정답입니다!")
        winlose = True
        break
    elif(answer > input_answer):
        print("입력하신 값보다 정답이 큽니다.")
    elif (answer < input_answer):
        print("입력하신 값보다 정답이 작습니다.")

if winlose:
    print("당신이 이겼습니다.")
else:
    print(f"틀렸습니다 정답은 {answer}입니다.")