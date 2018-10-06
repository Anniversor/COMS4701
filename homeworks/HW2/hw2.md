# Homework 2

## Part 1: Graph or Tree

1. 
![161538442248_.pic](/assets/161538442248_.pic.jpg)

2. A: {2} B: {1, 2} C: {1} D: {1, 2} E: {0, 1, 2} F: {1, 2}

3. 1 <font color=red>!!!</font>

## Part 2: Boring Matrix "Game"

1. 
![3554BBA8-C90D-4DAC-8BFA-210F813F594C](/assets/3554BBA8-C90D-4DAC-8BFA-210F813F594C.png)

2. |step|node|$\alpha$|$\beta$|value|children skipped|
   |---|---|---|---|---|---|
   |1|2|$-\infty$|$\infty$|3|-|
   |2|3|3|$\infty$|2|0, 8|
   |3|4|3|$\infty$|4|-|
   |4|5|4|$\infty$|4|1, 3|
   So the player A should choose the third row or the fourth row. <font color=red>!!!</font>
3. 
![E39568D7-36D5-4872-81D7-C41DF5B975B8](/assets/E39568D7-36D5-4872-81D7-C41DF5B975B8.png)
A should choose the third row, and the expected game value is $14/3$.

## Part 3: Immortal Race Car
1. 
![3D899982-78BA-45E3-849F-2B71172BC2A6](/assets/3D899982-78BA-45E3-849F-2B71172BC2A6.png)

2. $V^{\pi}(Cool)= 1 \times(2+0.8(V^{\pi}(Cool))$
$V^{\pi}(Warm)= 1 \times(2+0.8(V^{\pi}(Cool))$
$V^{\pi}(Off)= 0.25 \times(0+0.8(V^{\pi}(Warm))+0.75 \times (0+0.8(V^{\pi}(Warm))$
Solve the equations above, we can get:
$V^{\pi}(Cool)=10 $
$V^{\pi}(Warm)=10 $
$V^{\pi}(Off)=7.5 $
As for V(Cool) and V(Warm), because no matter the car is cool or warm, the policy just tells it to goes slow, so there is no chance for the car to change from warm to off, so they produce the same result for the car.
As for V(wait), The car just waits to get the chance to be warm again and during the wating there is no reward for the car, so the value of it is smaller than the other two values.

3. $V_{1}(Cool) = max(1 \times 2, 0.75\times 4+0.25\times 4) = max(2, 4) = 4$
   $V_{1}(Warm) = max(1\times 2, 0.5\times 4+0.5\times 2) = max(2, 3) = 3$
   $V_{1}(Off) = max(0) = 0$
The policy changes to direct the car to go fast when it's either cool or warm and wait when it's overheated.
For the state of Cool, the car can simply go fast than slow to gain more reward and there is no risk to be overheated. 
For the state of Warm, though there is risk of being overheated, the average reward of going fast is still greater than going slow. 
For the state of Off, the only action it can take is wait...

4. |State|$V_{0}(s)$|$V_{1}(s)$|$V_{2}(s)$|
   |---|---|---|---|
   |Cool|0|4|6.6|
   |Warm|0|3|5.2|
   |Off|0|0|0.6|
   $V_{1}(Cool) = max(1\times (2), 0.75\times 4+0.25\times 4) = max(2, 4) = 4$
   $V_{1}(Warm) = max(1\times 2, 0.5\times 4+0.5\times 2) = max(2, 3) = 3$
   $V_{1}(Off) = max(0) = 0$
   $V_{2}(Cool) = max(1\times (2+0.8\times 4), 0.75\times (4+0.8\times 3)+0.25\times (4+0.8\times 4)) = max(5.2, 6.6) = 6.6$
   $V_{2}(Warm) = max(0.5\times 2+0.5\times (4+0.8\times 3), 1\times (2+0.8\times 4)) = max(4.2, 5.2) = 5.2$
   $V_{2}(Off) = max(0.25\times (0+0.8\times 3)) = 0.6$

5. Based on the answer above, the optimal policy is that when car is Cool, go fast; when car is Warm, go slow; When car is Off, just wait.
For the policy in step 2, when the car is Cool it lets it go slow, which is suboptimal because the car will gain more if it goes fast. 
For the policy in step 3, when the car is Warm it lets it go fast. But the value of Cool is relatively big, and the value of Off is relatively very small. If we ask the car keep going fast when it's warm, the probability of getting overheated becomes larger and larger, and if it becomes Off it's really a big penalty. So when the car is Warm we should let it go slow to become cool and then go fast again.