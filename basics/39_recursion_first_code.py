# Recursion first time first code 
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
  
    show(100)#99,98,97,96,95,94,93,92,91,.....
