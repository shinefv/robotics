#スライムを倒し続けるだけのゲーム
import os
class Man():
    def __init__(self):
        self.name = "勇者"
        self.MAXHP=30
        self.HP = 30
        self.NATK = 10
        self.ATK = 10
    def damage(self,x):
        self.HP = self.HP - x
    def heal(self,x):
        self.HP = min(self.HP + x, self.MAXHP)
    def double(self):
        self.ATK = min(self.ATK * 2,1000)
class Slime():
    def __init__(self):
        self.MAXHP = 20
        self.HP = 20
        self.ATK = 5
        self.name="スライム"
    def damage(self,x):
        self.HP = self.HP - x
    def heal(self,x):
        self.HP = min(self.HP + x, self.MAXHP)
print("Start Slime Game")
print("Press ENTER: ")
def kirei():
    input()
    #windows の場合は、
    os.system("cls")
    #Mac, Linux の場合は、
    #os.system("clear")
kirei()
man = Man()
slime = Slime()
c = 1 
print(str(c)+"回戦目　敵が現れた")
counter = 0
while True:
    if slime.HP<=0:
        del slime
        slime = Slime()
        c += 1
        print(str(c)+"回戦目　敵が現れた")
    print("勇者　HP: "+str(man.HP)+"/"+str(man.MAXHP))
    print("")
    if counter > 0:
        counter += 1
    if counter is not 0 and counter%5 ==0:
        man.ATK=man.NATK
        print("勇者の攻撃力が元に戻った\n")
    #ユーザーの選択
    b=True
    while True:
        try:
            print("どうする？")
            a = input("攻撃: 1\n薬草 2\nスキル 3\n")
            if int(a) == 1:
                print("スライムに"+str(man.ATK)+"ダメージ")
                slime.damage(man.ATK)
                break
            elif int(a) == 2:
                man.heal(20)
                print("体力を20回復した")
                print("勇者　HP: "+str(man.HP)+"/"+str(man.MAXHP))
                break
            elif int(a)==3:
                man.double()
                print("攻撃力が"+str(man.ATK)+"になった")
                if counter ==0:
                    counter =1
                break
            else:
                print("1,2,3のいずれかを入力してください")
        except:
            print("数値を入力してください")

    #スライム倒し判定
    if slime.HP<=0:
        counter = 0
        man.ATK = man.NATK
        print("スライムを倒した")
        print("")
        print("勇者　HP: "+str(man.HP)+"/"+str(man.MAXHP))
        print("")
        b=True
        while True:
            print("ゲームを続けますか？")
            a = input("(YES 1/NO 0):")
            try:
                if int(a)==1:
                    print("続けます")
                    break
                elif int(a)==0:
                    print("終わります")
                    print("今回は"+str(c)+"回スライムを倒しました")
                    b=False
                    break
                else:
                    print("1か0を入力してください")
            except:
                print("数値を入力してください")
        if b:
            kirei()
            continue
        else:
            break
    #スライムの攻撃
    print("")
    print(slime.name+"の攻撃")
    print(slime.name+"は"+"勇者に"+str(slime.ATK)+"のダメージを与えた")
    man.damage(slime.ATK)

    #勇者死亡判定
    if man.HP<=0:
        print("---")
        print("勇者は死んだ")
        print("Game Over!")
        if c==1:
            print("スライムを一度も倒せませんでした")
        else:
            print("今回は"+str(c-1)+"回スライムを倒しました")
        break
    kirei()
