#tech.training@pragmatrixlearning.com
from os import system,name
def clean():
    if (name=='nt'):
        system('cls')
    else:
        system('clear')
    if(name=='nt'):
        system('mode con cols=120 lines=30')
    else:
        system("printf '\e[8;30;120t'")
import time
import random
names=['vettam','charlie','thattathin marayath','manichithrathazh','chithram','banglore days','premam','ustad hotel','devasuram','ravanaprabhu','narasimham','amaram','drishyam','kammatti padam','thanmathra','oru vadakkan veeragadha','sandesham','takeoff','virus','kireedam','ramji rao speaking','ohm shanthi oshana','thoovanathumpikal','maheshinte prathikaram','annayum rasoolum','joseph','amen','ezra','nort 24 kaatham','kala pani','neram','traffic','nadodikkattu','thondimuthalum driksakshiyum','vadakkunokkiyanthram','bharatham','njan prakashan','pranjiyettan and the saint','ennu ninte moideen','22 female kottayam','pattanapravesham','pazhashiraja','pattanapravesham','mumbai police','classmates','june','oru cbi diary kurippu','angamaly diaries','iyyobinte pusthakam','aadhyarathri','odiyan','spadikam','namukku parkkan munthirithoppukal','pulimurukan','perumthachan','vaishali','mrigaya','oru minnaminunginte nurungu vettam','thenmavin kombath','ozhimuri','kamaladalam','njan gandharvan','his highness abdulla','bhramaram','vadkkum nathan','kilukkam','adharvam','akkare akkare akkare','pappayude swantham appoos','yathrakarude sradhakku','spirit','left right left','celluloid','oru mexican aparatha','godha','ambili','athiran','gappi']
ext=0
while(ext!=1):
    clean()
    s=input("\n***************************************************Welcome To HANGMAN v0.3**********************************************\n------------------------------------------------------------------------------------------------------------------------\n\t\t\t\t\t\t+--------------------------+\n\t\t\t\t\t\t|     Choose an option     |\n\t\t\t\t\t\t+--------------------------+\n\t\t\t\t\t\t|\t 1.Play Game\t   |\n\t\t\t\t\t\t|\t 2.Add Name\t   |\n\t\t\t\t\t\t|\t 3.Credits\t   |\n\t\t\t\t\t\t|\t 4.Exit\t\t   |\n\t\t\t\t\t\t+--------------------------+\n Option : ")
    if(s=='1'):
        l=0
        while(l==0):
            clean()
            h=input("\n***************************************************Welcome To HANGMAN v0.3**********************************************\n------------------------------------------------------------------------------------------------------------------------\n\t\t\t\t\t\t+--------------------------+\n\t\t\t\t\t\t|     Choose an option     |\n\t\t\t\t\t\t+--------------------------+\n\t\t\t\t\t\t|\t 1.Easy\t\t   |\n\t\t\t\t\t\t|\t 2.Normal\t   |\n\t\t\t\t\t\t|\t 3.Hard\t\t   |\n\t\t\t\t\t\t+--------------------------+\n Difficulty : ")
            if(h=='1'):
                hard=10
                l=1
            elif(h=='2'):
                hard=5
                l=1
            elif(h=='3'):
                hard=3
                l=1
            else:
                clean()
                print("\tEnter a valid difficulty\n\n\t\t\tPlease wait......")
                time.sleep(2)
                l=0
        clean()
        if(len(names)<1):
            clean()
            print("Sorry Library is not found. Add names to play by choosing option 2 in the game........\n\n\t\t\tPlease Wait..........")
            time.sleep(3)
        else:
            clean()
            ans=[]
            vision=[]
            st=random.randrange(len(names))
            strings=names[st]
            string=''.join(e for e in strings if e.isalnum())
            for i in range(0,len(strings)):
                if(strings[i]==" "):
                    vision.append(" ")
                else:
                    vision.append('_')
            for i in vision:
                if(i!=" "):
                    ans.append(i)
            correct=0
            collected=""
            while(hard>0):
                clean()
                an=""
                print("No. of tries Remaining : ",hard)
                print("\n")
                for nl in vision:
                    if(nl==" "):
                        print("\n")
                    else:
                        print(nl,end=" ")
                print("\n")
                test=input("\nEnter Your Guess : ")
                if(test.isalnum()):
                    an=test.lower()
                else:
                    clean()
                    print(" The Character can not be parsed")
                    time.sleep(1)
                if(an not in collected):
                    for i in range(0,len(string)):
                        if(an==string[i]):
                            collected=collected+an
                            correct=correct+1
                            del ans[i]
                            ans.insert(i,an)
                            for v in range(0,len(strings)):
                                if(strings[v]==an):
                                    del vision[v]
                                    vision.insert(v,an.upper())
                            if(correct==len(string)):
                                break
                elif(an==""):
                    clean()
                    print("Empty value not acceptable..")
                    time.sleep(1)
                else:
                    clean()
                    print("The charcter is already found....")
                    time.sleep(1)
                if((an not in string) and (hard>0) and an!=""):
                    hard=hard-1
                    clean()
                    print("\t\tWRONG ANSWER\n\n\t\tPlease try again")
                    time.sleep(1)
                if(correct==len(string)):
                    break
                if(an==""):
                    clean()
                    print("No input Given")
            if(correct==len(string)):
                clean()
                print("You won\nAnswer is :",strings.upper(),"\n\n\nDo you wanna play again(yes=1)")
                pl=input()
                if(pl!='1'):
                    ext=1
            elif(hard==0):
                clean()
                print("You Lost\nAnswer is :",strings.upper(),"\n\n\nDo you wanna play again(yes=1)")
                pl=input()
                if(pl!='1'):
                    ext=1
    elif(s=='2'):
        clean()
        lf=0
        while(lf!='2'):
            clean()
            lf=input("\n***************************************************Welcome To HANGMAN v0.3**********************************************\n------------------------------------------------------------------------------------------------------------------------\n\t\t\t\t\t\t+--------------------------+\n\t\t\t\t\t\t|     Choose an option     |\n\t\t\t\t\t\t+--------------------------+\n\t\t\t\t\t\t|\t 1.Enter a name\t   |\n\t\t\t\t\t\t|\t 2.Go Back\t   |\n\t\t\t\t\t\t+--------------------------+\n Option : ")
            if(lf=='1'):
                clean()
                ipnm=input("\n***************************************************Welcome To LIBRARY***************************************************\n------------------------------------------------------------------------------------------------------------------------\n\n\t\tEnter a name :")
                temps=""
                for e in ipnm:
                    if(e.isalnum()):
                        temps=temps+(e.lower())
                    elif(e==" "):
                        temps=temps+" "
                if temps not in names:
                    names.append(temps)
    elif(s=='3'):
        clean()
        print(" ---\t---\t---\t---\t---\t------\t   ---         ---\t---\t---\t---\n | |\t| |    /   \\\t|  \\\t| |    /  _   \\    |  \\       /  |     /   \\    |  \\    | |\n | |\t| |   / / \\ \\   |   \\   | |   |\t / \   |   |   \\     /   |    / / \\ \\   |   \   | |\n | |____| |  / /___\\ \\  | |\\ \\  | |   |  |  \\__|   | |\\ \\   / /| |   / /___\\ \\  | |\\ \\  | |\n |  ____  | |  _____  | | | \\ \\ | |   |  |   __    | | \\ \\ / / | |  |  _____  | | | \\ \\ | |\n | |    | | | |     | | | |  \\ \\| |   \\  \\__/  |   | |  \\ _ /  | |  | |     | | | |  \\ \\| |\n |_|    |_| |_|     |_| |_|   \___|    \\____/-||   |_|         |_|  |_|     |_| |_|   \___|")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("Version 1.3\n\n\t\t\t\tcreated by JIGODU")
        time.sleep(3)
    elif(s=='4'):
        clean()
        print("\n\n\n\n\t\t\t\t\tThank you For Playing...........")
        time.sleep(5)
        ext=1
    else:
        clean()
        print("WRONG INPUT")
        time.sleep(2)
                        
                    