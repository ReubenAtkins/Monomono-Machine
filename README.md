# Monomono-Machine
Genetic algorithm to solve best coin amount for the Monomono Machine in Danganronpa: Trigger Happy Havoc.


I was curious about the monomono machine and how it works. Essentially, you have a set amount of coins and each time you receive a unique
item, your chance of obtaining another unique item decreases by roughly ~1.5%. You're then prompted and allowed to use multiple coins 
which increases the chance of a unique item by ~1.5%. It seemed to me that running 1 coin at a time was the best bet to receive the most
unique items. However, 1 coin at a time is painstakingly slow. So, I created an algorithm to determine the best coin amount per level, 
while also taking into effect "time" by how many rounds it took to receive a new unique item. The answer is around 2 coins, with a 
preference for (only slightly) higher amounts towards completion of all unique items.

Things to think about: 
  The fitness algorithm I'm using is certainly not the best. It's a bit flat for one, coin amt + 3 * rounds taken. It'd be nice to fit this
  more broadly into a range of 0-1 so as to allow quick selection of the next generation, but as it works pretty okay. 
  
  Similarly, I learned that COMPLETE GACHA is what this type of minigame is called, and actually became a banned practice in Japan. 
  Might be fun/interesting to look into what NEW methods game designers in Japan have come up with, and see how they compare.
