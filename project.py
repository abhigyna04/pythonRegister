class Register:
    name = " "
    rollno = " "
    email = " "
    pword = " "
    global d
    d = {}
    def __init__(self) -> None:
        pass
    
    def enterRoll(self,r):
        self.rollno = r
        d[r] = []
        return d 
    def enterName(self,n):
        d[self.rollno].append(n)
        return d       
    def enterEmail(self,e):
        d[self.rollno].append(e)
        return d
    def enterPword(self,p): 
        d[self.rollno].append(p)
        return d
    
r = Register()
print(r.enterRoll(input("Enter Roll number")))
print(r.enterName(input("Enter Your Name")))
print(r.enterEmail(input("Enter EMail Id")))
print(r.enterPword(input("Enter password")))

r.enterRoll('21B')
r.enterName('Pran')
r.enterEmail('xyz@ac.in')
r.enterPword('12345')

print(d)

class Login(Register):
    def __init__(self) -> None:
        pass
    def enterUrollno(self,urn):
        self.urn = urn
        if urn not in d.keys():
            print("User not found")
    def enterUpword(self,up):
        if up != d[self.urn][-1]:
            print("Incorrect password")
        else:
            print("Successfully Logged in!")

l = Login()
l.enterUrollno('21A')
l.enterUpword('123')
    
class Display(Register):
    def __init__(self) -> None:
        pass
    def userDetails(self,ur):
        self.ur = ur
        if ur not in d.keys():
            print("User not found. Register now!!")
        else:
            print("User name is : ",d[self.ur][0])
            print("Roll number is : ",self.ur)
            print("Email id is : ",d[self.ur][1])

dis = Display()
dis.userDetails('21A')

class Logout:
    def __init__(self) -> None:
        pass
    def exit(self):
        print("Logged out!")

lo = Logout()
lo.exit()


    