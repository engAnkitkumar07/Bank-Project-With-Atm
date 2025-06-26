#bank account..............................................................................................:
class Bank:
    def __init__(self,ac_num,name,balance,location):
        self.__ac_num=ac_num
        self.__name=name
        self.__balance=balance
        self.__address=location
    def deposit(self,amount):
        self.__balance=self.__balance+amount
    def withdraw(self,amount):
        if self.__balance<amount:
            print("Insufficient balance")
        else:
            self.__balance=self.__balance-amount
            print("Withdraw Successfully")
    def finalcheck(self):
        return self.__balance

    def passbook(self):
        print(f'A/c Number:-{self.__ac_num}\n'
              f'Holder Name:{self.__name}\n'
              f'Balance:{self.__balance}\n'
              f'Addreee:{self.__address}\n'
              f'City:Pokhrayan\n'
              f'IFSC Code:SBINOO9872\n'

                )
    def update_passbook(self):
        choice=int(input("Enter What You Want To Update..\n"
                         "1.Name\n"
                         "2.Account Number\n"
                         "3.Location\n"
                         "0.Don't Want Any Update"))
        if choice==1:
            name=input("What is Your Current Name In Passbook")
            new_name=input("Enter New Name")
            self.__name=new_name
            print(f"Name Updated Successfully...")
        elif choice==2:
            num=int(input("What Is Your Current A/c Number"))
            new_account=int(input("Enter New Account Number"))
            self.__ac_num=new_account
            print("A/c Number Updated Successfully...")
        elif choice==3:
            loc = input("What is Your Current location In Passbook")
            new_loc=input("Enter Your Prefer Location")
            self.__address=new_loc
            print("Location Updated Succesfully...")
        elif choice==0:
            return exit()
    def balance_checking(self):
        if balance>=2000:
            print("Congratulations--👍 ")
        else:
            print("You Are Not Able To Open A/c Sorry")
            print("ALERT!- Our Bank Policy First Amount You Have To Deposit>=2000")
            return exit()

    def account_need(self):
        if opt!=1:
            print("First Create Account After That Perform Operation \n"
                  "For Account Creation Press-->1 \n"
                  "Thank You")

    def need_atm(self):
        mode=input("Enter Your Mode Choice [Passbook or ATM]").strip().lower()
        if mode not in ["passbook","atm"]:
            print("Invalid Choice")
            mode="passbook"
        return mode

obj1=None
mode=None
while True:
    print("1.Create Account")
    print("2.Deposit Amount")
    print("3.Withdraw Amount")
    print("4.Final check")
    print("5.Passbook printing")
    print("6.Passbook Update")
    print("7. Issue ATM ")
    print("0.Exit..")


    opt=int(input("Enter Your Choice"))

    if opt==1:
        print("Your First Phase Creation Of Bank Account Have Your Required Details ")
        ac_num=int(input("Enter Your Choice Account Number"))
        name=input("Enter Candidate Name")

        balance=float(input("Enter Inital Balance>1500"))
        location= input("Enter Candidate Local Address")
        obj1=Bank(ac_num,name,balance,location)
        obj1.balance_checking()
        print("Account Has Been Opened Successfully--")
    elif obj1 is None:
        print("You Need First Create Account- Without Can't Use Any Another Option. Please Press 1 For A/c Opening")
    elif opt==2:
        if mode=='atm' or mode=='passbook':
            am=int(input("enter amount"))
            obj1.deposit(am)
            print("Deposit Successfully")
        else:
            print("Please Select First Your Mode Clicking By -->> 7 ")
    elif opt==3:

        if mode=='atm' or mode=='passbook':
            amt=int(input("Enter Amount for withdraw"))
            obj1.withdraw(amt)
        else:
            print("Please Select First Your Mode Clicking By -->> 7 ")

    elif opt==4:
        if mode=='atm' or mode=='passbook':
            print(obj1.finalcheck())
        else:
            print("Please Select First Your Mode Clicking By -->> 7 ")
    elif opt==5:
        if mode=='passbook':
            obj1.passbook()
    elif opt==6:
        if mode == 'passbook':
            obj1.update_passbook()
    elif opt==7:
        mode=obj1.need_atm()
        print(f"Your Mode Is -->> {mode.upper()}")

    elif opt==0:
        print("Account Closed Permanently! ")
        break
    else:
        print("Invalid Choice")

