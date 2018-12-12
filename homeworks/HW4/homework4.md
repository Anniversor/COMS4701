# Homework4

## Part 1: HMM Grading

1. $P(X_1=c|e_1)\propto P(e_1|c)P(X_1=c) = 0.8\times 0.5 = 0.4$
    $P(X_1=w|e_1)\propto P(e_1|w)(P(X_1=w) = 0.5\times 0.5 = 0.25$
    $P(X_1=c|e_1)= \frac{0.4}{0.25+0.4} = 0.615$
    $P(X_1=w|e_1)=\frac{0.25}{0.4+0.25} = 0.385$
    \
    $P(X_2=c|e_1,e_2)\propto P(e_2|c)\sum_{X_1}P(X_2=c|X_1)P(X_1|e_1)\propto 0.2\times (0.5\times 0.4+0.2\times 0.25) = 0.05$
    $P(X_2=w|e_1,e_2)\propto P(e_2|w)\sum_{X_1}P(X_2=w|X_1)P(X_1|e_1)\propto 0.5\times (0.5\times 0.4+ 0.8\times 0.25) = 0.2 $
    $P(X_2=c|e_1,e_2)= \frac{0.05}{0.05+0.2} = 0.2$
    $P(X_2=w|e_1,e_2)= \frac{0.2}{0.05+0.2} = 0.8$
    \
    $P(X_3=c|e_1,e_2,e_3)\propto P(e_3|c)\sum_{X_2}P(X_3=c|X_2)P(X_2|e_2) \propto 0.8\times (0.5\times 0.2+ 0.2\times 0.8) = 0.208 $
    $P(X_3=w|e_1,e_2,e_3)\propto P(e_3|w)\sum_{X_2}P(X_3=w|X_2)P(X_2|e_2) \propto 0.5\times (0.5\times 0.2+0.8\times 0.8) = 0.37$
    $P(X_3=c|e_1,e_2,e_3) = \frac{0.208}{0.208+0.37} = 0.360$

    $P(X_3=w|e_1,e_2,e_3) = 0.640$
    The autograder will grade the first part to right, and grade the second part and third part to wrong.

2. $m_0(c) = 0.5$
   $m_0(w) = 0.5$
   \
   $m_1(c) = P(e_1|c)m_0(c) = 0.8\times 0.5=0.4$
   $m_1(w) = P(e_1|w)m_0(w) = 0.5\times 0.5=0.25$
   \
   $m_2(c) = P(e_2|c)\max[P(c|c)m_1(c), P(c|w)m_1(w)]=0.2\times \max[0.5\times 0.4,0.2\times 0.25] = 0.2\times 0.2 =0.04$
   $m_2(w)=P(e_2|w)\max[P(w|c)m_1(c),P(w|w)m_1(w)]= 0.5\times \max[0.5\times 0.4, 0.8\times 0.25] = 0.5\times 0.2 = 0.1$
   So the autograder will grade the second part to wrong, but it can't determine whether the first part is right or wrong.

## Part 2: Independence Overload

1. $(A,B), (A,D)$
2. $(C,D), (A,D)$
3. None
4. $(A,E), (B,E)$
5. None
6. $P(A,C) = P(A)P(C|A) = \sum_{B}P(B)P(A)P(C|A,B)$
7. $P(C,D)=\sum_{A,B}P(C,D,A,B)=\sum_{A,B}P(A)P(B)P(C|A,B)P(D|B)$
8. $P(E|C)=\frac{P(E,C)}{P(C)}=\frac{\sum_{A,B,D}P(A)P(B)P(D|B)P(C|A,B)P(E|C,D)}{\sum_{A,B}P(A)P(B)P(C|A,B)}$
9. $P(A,B|C)=\frac{P(A,B,C)}{P(C)}=\frac{P(A)P(B)P(C|A,B)}{\sum_{A,B}P(A)P(B)P(C|A,B)}$
10. $P(A,D|C,E)=\frac{P(A,D,C,E)}{P(C,E)}=\frac{\sum_{B}P(A,B,C,D,E)}{\sum_{A,B,D}P(A,B,C,D,E)}=\frac{\sum_{B}P(A)P(B)P(C|A,B)P(D|B)P(E|C,D)}{\sum_{A,B,D}P(A)P(B)P(D|B)P(C|A,B)P(E|C,D)}$

## Part 3: Samples for Everyone
1. | C    | B    | P(B\|C) |
    | ---- | ---- | ------- |
    | +c   | +b   | 2/3      |
    | +c   | -b   | 1/3     |
    | -c   | +b   | 2/5     |
    | -c | -b | 3/5 |
2. Discard sample 1, 3, 5, 6, 7.
   The resulting distribution is:
   $\hat{P}(+e|-b,-c)= \frac{1}{3}$
   $\hat{P}(-e|-b,-c= \frac{2}{3}$

3. Sample in the order A, B, C, D, E; fix -b and -c whenever we get to them.
   Weight each sample by probability of -b, -c given the sample:
   - $(-a, -b, -c, -d, +e),\ w = P(-b)P(-c|-a,-b) = 0.75P(-b)$
   - $(+a,-b,-c,-d,-e),\ w=P(-b)P(-c|+a,-b) = 0.5P(-b)$
   - $(-a,-b,-c,-d,-e),\ w=P(-b)P(-c|-a,-b) =0.75P(-b)$
    Normalize the weights above, we can get:
    $\hat{P}(+e|-b,-c)=\frac{0.75P(-b)}{(0.75+0.5+0.75)P(-b)} = 0.375$
    $\hat{P}(-e|-b,-c)=\frac{(0.5+0.75)P(-b)}{(0.75+0.5+0.75)P(-b)} = 0.625$


