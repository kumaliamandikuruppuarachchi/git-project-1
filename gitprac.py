#here i copy and paste my past programme to check whether it is working
#shapes 8 file is uploading
num=int(input())
y=1
for a in range(num,0,-1):
    if y%2==1:
       print(" "*a,"*"*(2*y-1))
       y=y+1
    else:
        print(" "*a,"$"*(2*y-1))
        y=y+1