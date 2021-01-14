toDo=[]

def Enter(x):
    toDo.append(x)
def delete(pos):
    toDo.pop(pos)
def display():
    print("This is your To-Do List")
    p=1
    for i in toDo:
        print(p, ". ",i)
        p=p+1

ch='y'
while(ch=='y'):
    print("__________")
    print("TO-DO List")
    print("__________")
    print("1. Enter")
    print("2. Delete")
    print("3. Display")
    choice = int(input("What do you want to do? "))
    if(choice==1):
        task = input("Enter your task: ")
        Enter(task)
    elif(choice==2):
        op=int(input("Enter position of task you have completed: "))
        delete(op)
    elif(choice==3):
        display()
    else:
        print("Wrong input, try again")
    ch=input("Do you want to continue?(y/n) ")
 
    

