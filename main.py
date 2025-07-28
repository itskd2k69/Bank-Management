import json
import random
import string
from pathlib import Path



class Bank:
    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():

            with open(database) as fs:
                data = json.loads(fs.read())
        
        else:
            print("No such file exist")

    except Exception as err:
        print(f"An Exception occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountGenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num +spchar
        random.shuffle(id)
        return "".join(id)



    def Createaccount(self):
        info = {
            "name" : input("Enter Your name :"),
            "age" : int(input("Enter Your age :")),
            "e-mail" : input("Enter Your e-mail id :"),
            "pin" : int(input("Enter Your pin :")),
            "accountNo" : Bank.__accountGenerate(),
            "balance" : 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry You can not create your account")
        else:
            print("Account has been creted successfully 🙌")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please not down your Account Number")

            Bank.data.append(info)

            Bank.__update()

    def Depositemoney(self):
        accnumber = input("Enter Your Account Number :")
        pin = int(input("Enter Your pin aswell:"))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")

        else:
            amount = int(input("How much you want to deposite :"))

            if amount > 10000 or amount < 0:
                print("Sorry the amount is too much , you can deposite below 10,000 and above 0")

            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully 😘")

    def Withdrawmoney(self):
        accnumber = input("Enter Your Account Number :")
        pin = int(input("Enter Your pin aswell:"))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found")

        else:
            amount = int(input("How much you want to withdraw :"))

            if userdata[0]['balance'] < amount:
                print("Sorry yo do not have that much money 😉")
                

            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Your amount withdrew successfully 😘")

    def Showdwtails(self):
        accnumber = input("Enter Your Account Number :")
        pin = int(input("Enter Your pin aswell:"))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        print("Your information is as below \n\n\n:")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def UpdateDetails(self):
        accnumber = input("Enter Your Account Number :")
        pin = int(input("Enter Your pin aswell:"))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        
        if userdata == False:
            print("no such user data found 🤦‍♂️")

        else:
            print("you can not change the age ,account number, balance 😤 ")

            print("Fill the details for change or leave it empty if no change")

            newdata = {
                "name " : input("Tell new name or press enter to skip :"),
                "e-mail" : input("Tell your new e-mail or press enter to skip :"),
                "pin" : input("Enter new pin or press enter to skip :"),
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["e-mail"] == "":
                newdata["e-mail"] = userdata[0]["e-mail"]
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]

            newdata["age"] = userdata[0]["age"]
            newdata["accountNo"] = userdata[0]["accountNo"]
            newdata["balance"] = userdata[0]["balance"]

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] == newdata[i]
            
            Bank.__update()
            print("Detalis updated successfully 😉")


    def Delete(self):
        accnumber = input("Enter Your Account Number :")
        pin = int(input("Enter Your pin aswell:"))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no such data exist 😒")
        else:
            check = input("Press Y if you actually want to delete the account or press N")
            if check == 'n' or check == "N":
                print("bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully 😁")
                Bank.__update()
            


user = Bank()


print("Press 1 For creating an Account :")
print("Pres 2 For Depositing Money in the Bank :")
print("Press 3 For Withdrawing the Money :")
print("Press 4 For Details :")
print("Press 5 For Updating the Details :")
print("Press 6 For Deleting Your Account :")

check = int(input("Tell me What you want to do :"))


if check == 1:
    user.Createaccount()

if check == 2:
    user.Depositemoney()

if check == 3:
    user.Withdrawmoney()

if check == 4:
    user.Showdwtails()

if check == 5:
    user.UpdateDetails()

if check == 6:
    user.Delete()