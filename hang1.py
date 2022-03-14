import random
def hangman():
    f=open('words.txt',mode='r')
    data1=f.read()
    print(data1)
    f.close()
    word=random.choice(data1)
    chance=10
    str=''
    v=set('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        m_word=".."
        for letter in word:
            if letter in str:
                m_word=m_word+letter
            else:
                m_word=m_word+"_ "
        if m_word==word:
            print(m_word)
            print(" ** you won!!!!!*")
            break
        print("guess the word",m_word,)
        guess=input()
        if guess in v:
            str=str+guess
        else:
            print("enter velid charracter")
            guess=input()
        if guess not in word:
            chance=chance-1
            if chance ==9:
                print("8chance is left!!!!!!")
                print("-------------")
            if chance==8:
                print("6 chance is left!!!!!!")
                print("   o     ")
            if chance ==7:
                print("6 chance is left!!!!!!")
                print("   o    ")
                print("   |   ")
            if chance ==6:
                print("5 chance is left!!!!!!")
                print("   o    ")
                print("   |   ")
                print("  /   ")
            if chance ==5:
                print("4 chance is left!!!!!!")
                print("   o    ")
                print("   |   ")
                print("  / \  ")
                
            if chance ==4:
                print("3 chance is left!!!!!!")
                print("  \o    ")
                print("   |   ")
                print("  / \  ")
            if chance ==3:
                print("2 chance is left!!!!!!")
                print("  \o/   ")
                print("   |   ")
                print("  / \  ")
            if chance ==2:
                print("1 chance is left!!!!!!")
                print("  \o/ |  ")
                print("   |   ")
                print("  / \  ")
            if chance ==1:
                print("only one trun is left")
                print("  \o/__|")
                print("   |   ")
                print("  / \  ")
            if chance ==0:
                print("ooppssss sorrry you loss")
                break
name=input("enter your name.........")
print("WELCOME",name)
print("try to guess the words less then 10 times")
hangman()
