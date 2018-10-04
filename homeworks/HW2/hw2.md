# Homework 2

## Part 1: Graph or Tree
1. 
![161538442248_.pic](/assets/161538442248_.pic.jpg)

2. A: {2} B: {1, 2} C: {1} D: {1, 2} E: {0, 1, 2} F: {1, 2}

3. 1 <font color=red>!!!</font>


## Part 2: Boring Matrix "Game"
1. 
![3554BBA8-C90D-4DAC-8BFA-210F813F594C](/assets/3554BBA8-C90D-4DAC-8BFA-210F813F594C.png)
2. 
|step|node|$\alpha$|$\beta$|value|children skipped|
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

2. $V^{\pi}(Cool)=1.6 \ \ V^{\pi}(Warm)=1.6 \ \  V^{\pi}(Off)=0$
As for V(Coll) and V(Warm), because no matter car is cool or warm, it just goes slow, and there is no chance for the car to change from warm to off, so they produce the same result for the car. 
As for V(wait), The car just waits to get the chance to be warm again, so infact it's actually not working, so the value of it is zero and smaller than the other two values.

3. The policy changes to direct the car to go fast when it's either cool or warm and wait when it's overheated.
For the state of Cool, the car can simply go fast than slow to gain more reward and there is no risk to be overheated. 
For the state of Warm, though there is risk of being overheated, the average reward of going fast is still greater than going slow. 
For the state of Off, the only action it can take is wait...

4. 
5. 