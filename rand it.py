import random

num = None
lose = 5

while num != 3:
    print(f"Roll {num}")
    

    num = random.randint(0,30)
    if num == 3:
        print ("you rolled 3, you lose")
        break
    
        
        
