# Write a python programme to accept student number, name and marks in 3 subjects. 
# calculate total and average. print the student result based on the below condition.
# if avg >= 75 result is Distinction
# if avg >= 60 result is First class
# if avg >= 50 result is Second class
# if avg >= 35 result is Third class
# otherwise result is Fail

arr=[]
n=int(input("Enter Number of student: "))
#loop
for i in range(n):
    x=input("Enter Student Name: ")
    a=int(input("Enter Marks in subject-1: "))
    b=int(input("Enter Marks in subject-2: "))
    c=int(input("Enter Marks in subject-3: "))
    arr.append([x,a,b,c])
#total and average and result    
for i in range(n):
    total=(arr[i][1]+arr[i][2]+arr[i][3])
    avg=total/3
    print("Total and average marks of student Number",(i+1),"is",total,avg)
    if avg >=75:
      print("Result is Distinction for student",arr[i][0])
    elif avg >=60:
       print("Result is First Class for student",arr[i][0])
    elif avg >= 50:
       print("Result is Second Class for student",arr[i][0])  
    elif avg >= 35:
       print("Result is Third Class for student",arr[i][0])  
    else:
       print("Result is Fail for student",arr[i][0])  

                  


