'''# While loop
is_fail=True
i=1
# while condition:
    
while is_fail :
    if i%2==0:
     i=i+1
     continue
    print(f"{i}")
    i=i+1
    if i>=10:
     break
pin="1234"
trials=1
while trials<=3:
  input_pin=input(f"Trial-{trials} PIN: ")
  trials+=1
  if input_pin==pin:
    print("correct")
    break
  else:
    print("incorrect")'''
count=True
i=10
while count:
    if i<=10:
     i=i-1
     continue
    print(f"{i}")
    i=i-1
    if i<=10:
     break
