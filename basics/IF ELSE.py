#if True:
    #print("True")

#marks = input("What is your KCPE marks: ")
#marks = eval(marks)
#if marks <0 or marks >500:
    #print("Your marks are unrealistic")

    #if marks >= 350 and marks<=500:
           #print("congratulations,you are admitted")
    #else:
            #print("sorry,Try again")

        #read on if -elif -else statements
    #avg_marks = 70
avg_marks = int(input("avg_marks: "))
if avg_marks>=70 and avg_marks<=100:
    print("A")
elif avg_marks>=60:
        print("B")
elif avg_marks>=50:
        print("C")
elif avg_marks>=40:
        print("D")
else:
        print("F")
