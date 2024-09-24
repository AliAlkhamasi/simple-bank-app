import os
users = {}
def sign_up():
    os.system("clear")  
    while True:
        user = input("Skapa ett konto, ange 4 siffror: ")
        if len(user) == 4 and user.isdigit():
            if user in users:
                print("Kontot existerar redan,försök igen!")
            else:
                users[user] = 0.0
                print(f"konto: {user} registerat med ett saldo på 0.0")
                break
        else:
            print("ogiltig inmatning, vänligen skriv in 4 siffror!")


def deposit(user):
    os.system("clear")
    while True:
        try:
            amount = float(input("Hur mycket vill du sätta in: "))
            if amount < 0:
                print("ogiltigt värde")
            elif amount > 0:
                print(f"insättningen på {amount}SEK genomförd")
                users[user] += amount
            break
        except:
            print("ogiltig inmatning!")        
       


def withdraw(withdraw_user):
    os.system("clear")
    while True:
        try:
            amount = float(input("Hur mycket vill du ta ut?: "))
            if amount <0:
                print("Ogiltigt värde, vänligen ange ett värde över 0") 
            elif amount > users[withdraw_user]:
                print("Otillräckliga medel!")
            else:
                users[withdraw_user] -= amount  
                print(f"du tog ut {amount}SEK. nytt saldo {users[withdraw_user]}SEK")
            break
        except:
            print("ogiltig inmatning, ange siffervärde!")      
   


def balance(balance_user):
    os.system("clear")
    print(f"Ditt saldo är {users[balance_user]}")




def account_menu(acc_menu):
    while True:
        print(f"***KONTOMENY*** - {acc_menu}")
        print("1.Ta ut pengar\n"
             "2.Sätt in pengar \n"
             "3.Visa saldo\n"
             "4.Logga ut")
        choice = input("Menyval> ")
        if choice == "1":
            withdraw(acc_menu)
            continue
        if choice == "2":
            deposit(acc_menu)
            continue
        if choice == "3":
            balance(acc_menu)
            continue
        if choice == "4":
            os.system("clear")
            break
        else:
            print("ERROR! Välj alternativ 1-4!")




def admin():
   os.system("clear")
   admin_user = input("logga in med ditt fyrsiffriga nummer: ")
   if admin_user in users:
    print(f"inloggad på kontonummer {admin_user}")
    account_menu(admin_user)


   else:
    print("kontot finns inte!")
    pass


def mainmenu():
    while True:
        print("***HUVUDMENY***")
        print("1.skapa konto\n"
            "2.Administrera \n"
            "3.Avsluta programmet")
        val = input("Ange menyval> ")
        if val == "1":
            sign_up()
        elif val == "2":
            admin()
        elif val == "3":
            break
        else:
            print("ogiltig inmatning, Försök igen!")
           
mainmenu()  