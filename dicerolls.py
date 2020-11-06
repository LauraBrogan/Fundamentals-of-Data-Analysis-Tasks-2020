import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.style.use('ggplot')

np.random.seed(1738)
d1 = np.array([1, 2, 3, 4, 5, 6])
d2 = np.array([1, 2, 3, 4, 5, 6])
dice_1 = []
dice_2 = []
sums = []
for _ in range(500):
  roll_1 = np.random.choice(d1)
  roll_2 = np.random.choice(d2)
  dice_1.append(roll_1)
  dice_2.append(roll_2)
  sums.append(roll_1 + roll_2)






#import random
#first_roll = random.randint(1,6)
#second_roll = random.randint(1,6)

#comp_sum = first_roll +second_roll
#print(comp_sum)




#import numpy as np
#k=2
#n=1000
##rng = np.random.default_rng()
#mydict = dict(rng.multinomial(100,[1/6.]*6, size =3))
#print(mhydict)
#import random
#from collections import Counter
#sides = range(1,6)
#num_throws = 1000
#counter = Counter(random.choice(sides, k = num_throws))

#print(counter)
# create a dict
#d = {}

# iterate over all values you threw
#for num in [1,2,2,3,2,2,2,2,2,1,2,1,5,99]:
    # set a defaultvalue of 0 if key not exists
   # d.setdefault(num,0)
    # increment nums value by 1
   # d[num]+=1

#print(d)  # {1: 3, 2: 8, 3: 1, 5: 1, 99: 1}