for i in range(1,101):
    if i%7==0 or i%10==7 or i//10==7:
        continue
        i+=1
    else:
        print(i)
        i+=1
