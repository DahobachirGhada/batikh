import random
fruits = ['apple','mango','orange','peach','melon']
i=1
word = random.choice(fruits)
chance=len(word)+2
x = len(word)
print(word[0],'_'*(x-2),word[-1])
while chance>0 and i<len(word)-1:
    print('chances left :',chance)
    c=input()
    if c==word[i]:
        i+=1
    else:
        chance-=1
if i==len(word)-1 :
    print("you WIN!")
else: 
    print("WOP WOP WOOOOOP")