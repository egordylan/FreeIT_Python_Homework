# Это хотелось сделать с момента прослушивания интервью Романа К. у IT Beard

print("Foo - кратное 3. Bar - кратно 5. Foobar - кратно 3 и 5.")
print("Counting Foo:")
for i in range(0, 101, 3):
    print(i, end=" ")

print("\n\nCounting Bar:")
for i in range(0, 101, 5):  
    print(i, end=" ")
    
print("\n\nCounting Foobar: ") 
for i in range(0, 101):
    if i % 3 == 0 and i % 5 == 0:
      print(i,end = " ")
      
input("\n\nPress the enter key to exit.\n")
