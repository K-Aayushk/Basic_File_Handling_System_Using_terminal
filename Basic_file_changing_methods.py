class fileChanger:
    def __init__(self,file):
        self.file=file
        
        
    def r(self):
        f=open(f"{self.file}","r")
        print(f.read())
        f.close()
        
    def w(self):
        with open(f"{self.file}","w") as f:
            inp=input("Enter the Values : ")
            fi=f.write(inp)
            print("Changes has Been Made!")
    def empty(self):
        with open(f"{self.file}","r") as f:
            l=f.read()
            if(l!=""):
                with open(f"{self.file}","w") as f1:
                    f1.write("")
                    print("File is now emptied!")
            else:
                print("File is already empty!")
    
    @staticmethod
    def static():
        print("Please include the file extension also!")
p=fileChanger.static()
inpp=input("Enter the file location: ")
command=fileChanger(inpp)
dic={"Read":"command.r()",
     "Write":"command.w()",
     "Empty":"command.empty"}
print(dic)
inp=input("Enter the command? ")
exec(inp)


        