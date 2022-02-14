import pyinputplus as pyip
import random, time
correct = 0
for question in range(10):
    try:
        num1 = random.randint(1,9)
        num2 = random.randint(1,9)
        result = num1*num2
        prompt = f'{num1} x {num2} ='
        try:
            answer = pyip.inputInt(prompt, min=result, max=result, timeout=8, limit=3)
        except pyip.TimeoutException:
            print('Out of time!')
        except pyip.RetryLimitException:
            print('Out of tries!')
        else:
            print('Correct!')
            correct+= 1
        time.sleep(1)
    except KeyboardInterrupt:
        print('\nKeep calculating!')
print(f'Score: {correct} / 10') 
