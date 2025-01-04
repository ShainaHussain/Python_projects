from random import shuffle
qus = [
    ("What is name of your country","India"),
    ("What is the capital of your country","New Delhi"),
    ("What is the national flower","Lotus"),
    ("What is the name of your national animal","Tiger"),
    ("What is your national bird's name","Peacock"),
    ("What is your national flag","Tiranga")
]
shuffle(qus)
right = 0
wrong = 0
for question, right_ans in qus:
    ans = input(question + " ")
    if ans.title() == right_ans:
        right +=1
    else:
        print("No the right ans is:",right_ans)
        wrong +=1
print("Congratulation !")
print("You gave ",right , "right answers and",wrong,"wrong answers")