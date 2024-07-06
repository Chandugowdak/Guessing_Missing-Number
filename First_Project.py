class First_Project:
    def Accept_Values(self , a,i):
        while(i<3):
            b=int(input("Enter the Gussing Number : "))
            if b==a:
                print("You Won")
                break
            else:
                print("You Can Try Once More")
                i+=1
Object = First_Project()
Object.Accept_Values(143,0)        