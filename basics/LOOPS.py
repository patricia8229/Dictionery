#while loop
#a while loop repeats execution of its block until the condition given is false

a = 0
while a <100:
    print ("Patricia Wanjiku")
    a += 1
    print (a)
print ("Patricia Wanjiku")

savedpin = "9999"
tries =3


attempts =0
current = input ("enter pin")
tries -=1
#print ("before loop",attempts)
while current != savedpin and tries > 0:
    current = input ("enter pin")
    tries -= 1

if current != savedpin:
    print("card blocked")
else:
    print ("welcome, proceed")


