Weeks=int(input("Enter no. of weeks:-")) 
X=float(input("Enter firs week's amount:-")) 
a=float(input()) 
b=float(input()) 
c=float(input()) 
Week_1=X-((a+b+c)*(X/100)) 
Total=Weeks*Week_1 
print("Total amount:-",Total) 
