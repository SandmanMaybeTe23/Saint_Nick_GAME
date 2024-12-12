## Def
def input_int(text):
    while True:
        try:
            return int(input(text))
        except:
            print("You need to write a number paly.")


def  input_str(text):
    while True:
        try:
            return str(input(text))
        except:
            print("forget the number use your words")
        

##Imports
from random import randint


##Player
NamePlayer=0
AttackPlayer=1
HpPlayer=10
ArmorPlayer=0
ChanceOFmiss=0


##Loot
AttacksMelee1=True
AttacksMelee2=False
AttacksMelee3=False

AttacksRange1=False
AttacksRange2=False
AttacksRange3=False

AttacksLOL1=False
AttacksLOL2=False


Attacks=["Pun",]

##looting
Loot1=0


##Enemy's
Enemy1_HP=5
Enemy1_Atk=0
BattleOfBag=0
BattleRound1=0


Enemy2_HP=10
Enemy2_Atk=2
BattleRound2=0

Enemy3_HP=10
Enemy3_Atk=4
BattleRound3=0

Enemy4_HP=15
Enemy4_Atk=6
BattleRound4=0

Saint5_HP=20
Saint5_Atk=10
BattleRound5=0

##Game
round=0
Ready=0
pickAtk1=0
Crit_pickAtk1=0
Tur_pickAtk1=0
Enemy1_Atk_face=0



print("Kid Your Going TO FIGHT THE BOX AND Evenly saint Nickolas HoHoHo")
NamePlayer=input("SO What Is You Name HoHoHo ")


print("")


print("So This is the Battle of Bag HoHoHo")
BattleOfBag=input(f"Are you Ready[Y] {NamePlayer} HoHoHo ").upper()
if BattleOfBag !="Y":
    BattleOfBag="Y"
else:
    print


while BattleOfBag=="Y":
    BattleRound1 +=1
    print(f"Enemy Hp{Enemy1_HP}")
    print(f"Enemy Atk {Enemy1_Atk}")
    if BattleRound1==1:
        print("So You will always begin the round")
        Tur_pickAtk1=True
    elif BattleRound1 ==2:
        print("alright i am going to give you a critical attack")
        print("it normally dose double dmg maybe more")
        Crit_pickAtk1=True        
    else:
        print()

    while Tur_pickAtk1==True:
        print("so right now is your attack face")
        print("Below this text are your attacks")
        for attack in Attacks:
            print(attack)
        print("now you see your attacks right now is only pun")
        Pick_AttackBag=input_int("To pick Pun Write [1] Buy THE Way is dose 2 dmg ")
        if Pick_AttackBag ==1:
            if AttacksMelee1==True:
                Enemy1_HP -= 2 * AttackPlayer 
                Tur_pickAtk1=False
                Enemy1_Atk_face=True
                Pick_AttackBag =0
            elif AttacksMelee2==True:
                 Enemy1_HP -= 5 * AttackPlayer 
                 Tur_pickAtk1=False
                 Enemy1_Atk_face=True
                 Pick_AttackBag =0
            elif AttacksMelee3==True: 
                Enemy1_HP -= 8* AttackPlayer 
                Tur_pickAtk1=False
                Enemy1_Atk_face=True
                Pick_AttackBag =0
            else:
                print()

            while Crit_pickAtk1==True:
                for attack in Attacks:
                    print(attack)
                print("alright pick pun and unleash the crit")
                Pick_AttackBagCrit=input_int("To pick Pun Write [1] Buy THE Way is dose 2 dmg ")
                if Pick_AttackBagCrit == 1:
                    Enemy1_HP -=4*AttackPlayer 
                    print("you attack bag with a crit")
                else:
                    print

                
              
            while Enemy1_Atk_face==True:
                if BattleOfBag==1:
                    print("Alright Now is THE Enemy Attack Face")
                    Enemy1_Atk_move=True
                else:
                    print()
                    Enemy1_Atk_move=True
                while Enemy1_Atk_move==True:
                    AttackEnemy=input=randint(1,3)
                    if AttackEnemy==1:
                        HpPlayer -= Enemy1_Atk * 0.5
                        print("Enemy Did a weak Attack")
                        Enemy1_Atk_move=False
                        Enemy1_Atk_face=False
                    elif AttackEnemy==2:
                        HpPlayer -= Enemy1_Atk
                        print("Enemy Did a Normal Attack")
                        Enemy1_Atk_move=False
                        Enemy1_Atk_face=False
                    elif AttackEnemy ==3:
                        HpPlayer -= Enemy1_Atk * 1.5
                        ("Enemy Did a Crit Attack")
                        Enemy1_Atk_move=False
                        Enemy1_Atk_face=False
                    else:
                        print()

                    if Enemy1_HP<0:
                        print({BattleRound1})
                        print("You Defeated Bag ")
                        print("ok now to the good stuff the loot ")
                        print("first item is a dumbBell it will increase your melee dmg")
                        print("second item is a WaterGun it can do some good dmg but can miss")
                        print(" Third i tell you a joke HoHoHo")
                        Loot1=input_int("so what will it be [1] [2] or [3]")
                        if Loot1== 1:
                            AttackPlayer+=1
                            print("you have picket DumbBell")
                        elif Loot1 == 2:
                            Attacks.append("WaterGun")
                            print(" you have picket WaterGun")
                            AttacksRange1=True
                        elif Loot1 == 3:
                            Attacks.append("Deez")
                            AttacksLOL1=True
                            print("ok here it i have deez ")


                        Feeling=input_str=print("How do you feel")
                        BattleOfBag=False
                        MainGame=True
                    else:
                        print()
                        

                    
            

                


            
            
                 


            


            

        
        









while MainGame==True:
    print(f"Welcome {NamePlayer} To Your Doom HoHoHo")
    print(" Btw this was a False Flag Operation HaHa HoHoHo")
    print(" That is Right im was always Santa HaHa HoHoHo")

    print(r""" 
_________ .__          .__          __                          __________                            
\_   ___ \|  |_________|__| _______/  |_  _____   ____   ______ \______   \__ _________  ____   ____  
/    \  \/|  |  \_  __ \  |/  ___/\   __\/     \_/ __ \ /  ___/  |     ___/  |  \_  __ \/ ___\_/ __ \ 
\     \___|   Y  \  | \/  |\___ \  |  | |  Y Y  \  ___/ \___ \   |    |   |  |  /|  | \/ /_/  >  ___/ 
 \______  /___|  /__|  |__/____  > |__| |__|_|  /\___  >____  >  |____|   |____/ |__|  \___  / \___  >
        \/     \/              \/             \/     \/     \/                        /_____/      \/ 
""")

    Ready=input(f"are Your Ready{NamePlayer} [Y]").upper()
    if Ready !="Y":
        Ready="Y"
    else:
        print
 

    while Ready=="Y":
        round+=1
        print("")