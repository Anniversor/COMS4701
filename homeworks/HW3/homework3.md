# Homework 3

Haoyu Yan 

hy2574

## Written Portion

### Part 1

1. T (cool, slow, cool) = 1  R (cool, slow, cool) = +2

   T (cool, fast, cool) = 1/3  R (cool, fast, cool) = +2

   T (cool, fast, warm) = 2/3  R (cool, fast, warm) = +4

   T (warm, slow, cool) = 1  R (warm, slow, cool) = +2

   T (warm, fast, off) = 1  R (warm, fast, off) = 0

   T (off, wait, off) = 1  R (off, wait, off) = 0

   $V^{*}(cool) = 𝑚𝑎𝑥_{a} [1*(2+0.5* V^{*}(cool)), 1/3*(2+0.5* V^{*}(cool))+2/3*(4+0.5 * V ^{*} (warm))]$

   $V^{*}(warm) = 𝑚𝑎𝑥_{a}[1*(2+0.5* V*(cool)), 1*(0+0.5* V*(off))]$

   $V^{*}(off) = 𝑚𝑎𝑥_{a}[1*(0+0.5* V^{*}(off))]$

   Solve the equations above, we can get that:

   $V^{*}(cool) = 6$  $V^{*}(warm) = 5$  $V^{*}(off) = 0$

2. |     Transition      | Q(cool, slow) | Q(cool, fast) | Q(warm, slow) | Q(warm, fast) | Q(off, wait) |
   | :-----------------: | :-----------: | :-----------: | :-----------: | :-----------: | :----------: |
   | (cool,slow,cool,+2) |       1       |       0       |       0       |       0       |      0       |
   | (cool,fast,cool,+2) |       1       |      1.5      |       0       |       0       |      0       |
   | (cool,fast,warm,+4) |       1       |     2.75      |       0       |       0       |      0       |
   | (warm,slow,cool,+2) |       1       |     2.75      |     2.375     |       0       |      0       |
   | (cool,fast,warm,+4) |       1       |    4.5625     |     2.375     |       0       |      0       |
   |  (warm,fast,off,0)  |       1       |    4.5625     |     2.375     |       0       |      0       |
   |  (off,wait,off,0)   |       1       |    4.5625     |     2.375     |       0       |      0       |

3. When cool, go fast; when warm, go slow; when off, wait.

### Part 2

1. |  B   |  C   | P(B,C) |
   | :--: | :--: | :----: |
   |  +b  |  +c  | 0.0125 |
   |  +b  |  -c  | 0.0375 |
   |  -b  |  +c  | 0.2375 |
   |  -b  |  -c  | 0.7125 |

2. $P(B=+b) = 0.05$   $P(B=-b)  = 0.95$   $P(C=+c) = 0.25$   $P(C=-c) = 0.75$

   $P(+b)P(+c) = 0.05 * 0.25 = 0.0125 = P(+b, +c)$

   We can also get that P(+b)P(-c) = P(+b, -c), P(-b)P(+c) = P(-b, +c), P(-b)P(-c) = P(-b, -c)

   So we can get that $P(B)P(C) = P(B, C)$, which means that B are independent of C.

3. $P(A= +a) = P(+a, +b, +c) + P(+a, +b, -c) + P(+a, -b, +c) + P(+a, -b, -c) = 0.8025$

4. $P(+b | A = +a) = P(+a, +b) / P(+a) = 0.0025/0.8025 = 0.00312$ $P(-b|A = +a) = 1-P(+b | A = +a) = 0.99688$

5. $P(+b | +a, -c) = \frac{P(+a, +b, -c)}{P(+a, -c)} = \frac{0.0025}{0.0025+0.6125}=0.00407$ 

   It is now higher. Because we now know that the weather is nice and you arrive on time, since the weather can't stop you arrive on time, we now have more tolerance towards the MTA, which means that we allow it to be more naughty, so the probability of delay increases. For analogy, we need a project done, and there are two workers A and B, if A is sick (bad weather), B have to do more work (lower probability of MTA to delay), but if A is healthy and hardworking (Great weather), B can do less work (higher probability of MTA to delay).

### Part 3

1. | $X_{1}$ | $X_{2}$ | $P(X_{1}, X_{2})$ |
   | :-----: | :-----: | :---------------: |
   |  cool   |  cool   |       0.125       |
   |  cool   |  warm   |       0.375       |
   |  warm   |  cool   |        0.1        |
   |  warm   |  warm   |        0.3        |
   |  warm   |   off   |        0.1        |

2. | $X_{2}$ | $P(X_{2})$ |
   | :-----: | :--------: |
   |  cool   |   0.225    |
   |  warm   |   0.675    |
   |   off   |    0.1     |

3. $X_{3} ∐ X_{1}|X_{2}$, $X_{1}∐X_{3}|X_{2}$

   $P(X_{3}|X_{1}, X_{2}) = P(X_3|X_2)$

   | $X_2$ | $X_3$ | $P(X_3|X_1,X_2)$ |
   | :---: | :---: | :--------------: |
   | cool  | cool  |       0.25       |
   | cool  | warm  |       0.75       |
   | warm  | cool  |       0.2        |
   | warm  | warm  |       0.6        |
   | warm  |  off  |       0.2        |
   |  off  | warm  |       0.2        |
   |  off  |  off  |       0.8        |

   $P(X_1|X_3,X_2) = P(X_1|X_2)=\frac{P(X_1,X_2)}{P(X_2)}$

   | $X_1$ | $X_2$ | $P(X_1|X_3,X_2)$ |
   | :---: | :---: | :--------------: |
   | cool  | cool  |       5/9        |
   | cool  | warm  |       5/9        |
   | warm  | cool  |       4/9        |
   | warm  | warm  |       4/9        |
   | warm  |  off  |        1         |

4. When $n$ is large enough, we have $P(X_n) = P(X_{n-1})$

   $P_{\infty}(cool) = P(cool| cool) P_{\infty}(cool) + P(cool| warm) P_{\infty}(warm)$

   $P_{\infty}(warm) = P(warm| cool) P_{\infty}(cool) + P(warm| warm) P_{\infty}(warm) + P(warm| off) P_{\infty}(off)$

   $P_{\infty}(off) = P(off| warm) P_{\infty}(warm) + P(off| off) P_{\infty}(off)$

   $P_{\infty}(cool) + P_{\infty}(warm) + P_{\infty}(off) = 1$

   Solve the equations above, we can get:

   $P_{\infty}(cool) = \frac{2}{17}$

   $P_{\infty}(warm) = \frac{15}{34}$

   $P_{\infty}(warm) = \frac{15}{34}$

### Part 4

1. | $X_{t+1}$ | $P(X_{t+1}|X_{t})$ |
   | :-------: | :----------------: |
   |   (1,0)   |        1/2         |
   |   (1,1)   |         1          |

   | $E_{t}$ | $P(E_t|X_t)$ |
   | :-----: | :----------: |
   |    S    |     1/2      |
   |    C    |     1/2      |

2. | $X_1$ | $P(X_1|plant)$ |
   | :---: | :------------: |
   | (1,2) |      1/3       |
   | (2,2) |      1/3       |
   | (3,1) |      1/3       |

3. $P(X_2|e_1) = \sum_{x1}P(X_2|X_1)P(X_1|e_1)$ 

   $B(X_2) = P(X_2|e_1,e_2) \propto P( e_2|X_2)P(X_2|e_1) $

   And we know that only when $X_2 \in { (1,2), (2,2), (3,1) }$ , $P(e_2|X_2) != 0 $ , So we only need to calculate these three beliefs. 

   $P(X_2 = (1,2),(2,2),(3,1)|e_1, e_2) \propto (1*2/9, 1*2/9, 1*1/9) = (2/9, 2/9,1/9)$

   So we can get that:

   $P(X_2 = (1,2),(2,2),(3,1)|e_1, e_2) = (2/5, 2/5, 1/5)$ 

4. The state for $X_3$ is $(1,1)$

5. From 4 we know $P(X_3 = (1,1)|plant, plant, sofa ) = 1$

   $P(X_4=(1,0),(1,1)|plant, plant, sofa,sofa) \propto P(sofa|X_4 ) \sum_{x3}P(X_4|X_3)P(X_3|plant, plant, sofa) = (1/2 * 1/4, 1*1/4)$

   So we can get that:

   $P(X_4=(1,0),(1,1)|plant, plant, sofa,sofa) = (1/3, 2/3)$


