#スライムを倒し続けるだけのゲーム
import os

class Character():
    def __init__(self):
        self.name = ""
        self._MAXHP = 0
        self._MAXMP = 0
        self.HP = 0
        self.MP = 0
        self._NATK = 0
        self.ATK = 0
        self.DEF = 0
        self.counter = 0
        self.EXP = 0
        self.level = 1
    def heal(self,x):
        self.HP = min(self.HP + x, self._MAXHP)
        print("体力が"+str(x)+"回復した")
        
    def reset(self):
        self.ATK = self._NATK
    def fullreset(self):
        self.HP = self._MAXHP
        self.MP = self._MAXMP
        self.ATK = self._NATK
    def attack(self,x):
        print("")
        print(str(self.name)+"の攻撃")
        print(str(x.name)+"に"+str(max(0,self.ATK-x.DEF))+"のダメージ")
        x.HP =  x.HP - max(0,self.ATK-x.DEF)
    def getinfo(self):
        print(str(self.name)+"Lv."+str(self._level)+"　HP: "+str(self.HP)+"/"+str(self._MAXHP)+"　MP: "+str(self.MP)+"/"+str(self._MAXMP))
    def turn(self):
        self.getinfo()
        print("")
        if self.counter > 0:
            self.counter += 1
        if self.counter is not 0 and self.counter%5 ==0:
            self.ATK=self._NATK
            print(str(self.name)+"の攻撃力が元に戻った\n")

        
class Man(Character):
    def __init__(self):
        self.name = "勇者"
        self._MAXHP=12
        self._MAXMP = 0
        self._NATK = 10
        
        self.HP = 6
        self.MP = 0
        self.ATK = 20
        self.DEF = 0
        self.counter = 0
        self.EXP = 0
        self._level = 1
    def double(self):
        self.counter  = 1
        self.ATK = min(self.ATK * 2,1000)
        print("攻撃力が"+str(self.ATK)+"になった")
    def levelup(self):
        self._NATK += 1
        self._MAXHP += 2
        self.DEF += 1
        self._level += 1
    def win(self,x):
        self.EXP += x.EXP
        while self._level ** 3 < self.EXP:
            self.levelup()
            print("\nレベルアップ")
            print(str(self.name)+"はレベル"+str(self._level)+"になった")
            input()
class Slime(Character):
    def __init__(self):
        self.name="スライム"
        self._MAXHP = 20
        self._MAXMP = 0
        self._NATK = 5
        
        self.HP = 20
        self.MP = 0
        self.ATK = 5
        self.DEF = 0
        self.EXP = 5

def kirei():
    #input()
    #windows の場合は、
    #os.system("cls")
    #Mac, Linux の場合は、
    os.system("clear")
hope ="""
 ___  ___  ________  ________  _______      
|\  \|\  \|\   __  \|\   __  \|\  ___ \     
\ \  \\\  \ \  \|\  \ \  \|\  \ \   __/|    
 \ \   __  \ \  \\\  \ \   ____\ \  \_|/__  
  \ \  \ \  \ \  \\\  \ \  \___|\ \  \_|\ \ 
   \ \__\ \__\ \_______\ \__\    \ \_______
    \|__|\|__|\|_______|\|__|     \|_______|
"""

azure ="""
 ________  ________  ___  ___  ________  _______      
|\   __  \|\_____  \|\  \|\  \|\   __  \|\  ___ \     
\ \  \|\  \\|___/  /\ \  \\\  \ \  \|\  \ \   __/|    
 \ \   __  \   /  / /\ \  \\\  \ \   _  _\ \  \_|/__  
  \ \  \ \  \ /  /_/__\ \  \\\  \ \  \\  \\ \  \_|\ \ 
   \ \__\ \__\\________\ \_______\ \__\\ _\\ \_______
    \|__|\|__|\|_______|\|_______|\|__|\|__|\|_______| """
class User():
    def __init__(self):
        self.__condition = 1
        self.c = 1
        self.man = Man()
        self.slime = Slime()
    def getcondition(self):
        return self.__condition
    def menu(self):
        self.man
        if self.__condition == 1:
            while True:
                kirei()
                print("---希望の町---\n")
                print(hope)
                print("どうする？")
                self.man.getinfo()
                a = input("冒険に出る 1\n宿屋に泊まる 2\n終了 3\n")
                try:
                    a = int(a)
                except:
                    print("数値を入力してください")
                    continue
                if a == 1:
                    self.__condition = 0
                    break

                elif a == 2:
                    self.man.fullreset()
                    print("体力が全回復した")
                    self.man.getinfo()
                    continue

                elif int(a)==3:
                    print("")
                    self.man.getinfo()
                    print("")
                    b=True
                    while True:
                        print("ゲームを続けますか？")
                        a = input("(YES 1/NO 0):")
                        try:
                            a=int(a)
                        except:
                            print("数値を入力してください")
                            continue
                        if a==1:
                            print("続けます")
                            break
                        elif a==0:
                            print("終わります")
                            print("今回は"+str(self.c - 1)+"回スライムを倒しました")
                            b=False
                            break
                        else:
                            print("1か0を入力してください")
                    if b:
                        kirei()
                        continue
                    else:
                        self.__condition = 2
                        break
                else:
                    print("1,2,3のいずれかを入力してください")
            
            
        elif self.__condition == 0:
            self.game()
            while True:
                if self.__condition == 2:
                    break
                kirei()
                print("---冒険: 蒼穹の草原---")
                print(azure)
                self.man.getinfo()
                print("")
                print("(どうする？)")
                print("冒険を続ける 1\n町に戻る 2\n道具 3\n")
                a = input("選択: ")
                try:
                    a = int(a)
                except:
                    print("数値を入力してください214")
                    continue
                if a == 1:
                    break
                elif a == 2:
                    self.__condition = 1
                    print("町に戻った")
                    input()
                    break
                elif a == 3:
                    self.man.heal(20)
                    self.man.getinfo()
                    input()
                    continue
                else:
                    print("1,2のいずれかを入力してください")            
    def select(self,x,y):
        while True:
            kirei()
            print("---冒険: 蒼穹の草原---")
            print(azure)
            self.man.getinfo()
            print("(どうする？)")
            print("攻撃 1\n道具 2\nスキル 3\n")

            a = input("選択: ")
            try:
                a = int(a)
            except:
                print("数値を入力してください")
                continue

            if a == 1:
                x.attack(y)
                break

            elif a == 2:
                x.heal(20)
                print("勇者　HP: "+str(x.HP)+"/"+str(x._MAXHP))
                break

            elif a==3:
                x.double()
                break

            else:
                print("1,2,3のいずれかを入力してください")
            
            
    def game(self):
        kirei()
        print("---冒険: 蒼穹の草原---")
        print(azure)
        if self.c ==1:
            input()
            print(str(self.c)+"回戦目　敵が現れた")
            input()
        kirei()
        while True:
            print("---冒険: 蒼穹の草原---")
            print(azure)
            if self.slime.HP<=0:
                self.slime.fullreset()
                input()
                print(str(self.c)+"回戦目　敵が現れた")
                input()
            self.man.turn()
            #ユーザーの選択
            self.select(self.man,self.slime)
            input()

            #スライム倒し判定dead.
            if self.slime.HP<=0:
                self.man.reset()
                self.c += 1
                print("スライムを倒した")
                input()
                kirei()
                self.man.win(self.slime)
                print("")
                self.man.getinfo()
                print("")
                break
                

            #スライムの攻撃
            kirei()
            print("---冒険: 蒼穹の草原---")
            print(azure)
            self.slime.attack(self.man)
            input()
            
            
            #勇者死亡判定
            if self.man.HP<=0:
                print("---")
                print("勇者は死んだ")
                print("Game Over!")
                if self.c==1:
                    print("スライムを一度も倒せませんでした")
                else:
                    print("今回は"+str(self.c - 1)+"回スライムを倒しました")
                self.__condition = 2
                break
            kirei()
kirei()
print("""
 _____ ______   ________  ________  ___  ___  ___    _______     
|\   _ \  _   \|\   __  \|\   ____\|\  \|\  \|\  \  /  ___  \    
\ \  \\\__\ \  \ \  \|\  \ \  \___|\ \  \\\  \ \  \/__/|_/  /|   
 \ \  \\|__| \  \ \   __  \ \  \    \ \   __  \ \  \__|//  / /   
  \ \  \    \ \  \ \  \ \  \ \  \____\ \  \ \  \ \  \  /  /_/__  
   \ \__\    \ \__\ \__\ \__\ \_______\ \__\ \__\ \__\|\________\\
    \|__|     \|__|\|__|\|__|\|_______|\|__|\|__|\|__| \|_______|  """)

print("\n始めるにはエンターを2回押してください... ")
input()
user = User()
while True:
    user.menu()
    if user.getcondition() == 2:
        break
