## Pattern searching algorithms (Naive algorithm and Sunday's algorithm)
### 1. alphabet, text, pattern 
Let A be a set of elements (eg. letters), called the alphabet.

Let T be a sequence of elements that belong to the alphabet, called the text. Elements from the text are indexed from 0 to |T|.

Let P be a sequence of elements that belong to the alphabet, called the pattern. Elements from the pattern are indexed from 0 to |P|.
#### 1.1. Example (alphabet, text, pattern)
*A = {A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z}* and *|A| = 26*

*T = AABACABAC* and *|T| = 9* 

*P = BAC* and *|P| = 3* 

### 2. Naive algorithm O(|P||T|)
#### 2.1. matchesAt method
Pattern *P* matches *T* at position *p* if T[*p* + *i*] = P[*i*], *p* = 0, 1, 2, ..., |*P*| - 2, |*P*| - 1   

matchesAt condition: *p* < |*T*| - 1

optimistic scenario: 1 comparison when T[p + 0] != P[0]

pesimistic scenario: (|T| - |P| + 1) * |P| comparisons
#### 2.2. Example (matchesAt method) - pattern does not match text
matchesAt(T, P, p), *T = AABACABAC*, *P = AAC*, *p* = 0 returns **false**


T[0 + 0] = A and P[0] = A 

T[0 + 1] = A and P[1] = A

T[0 + 2] = B and P[2] = C

AAC does not match AAB
#### 2.3. Example (matchesAt pattern matches text
matchesAt(T, P, p), *T = AABACABAC*, *P = BAC*, *p* = 2 returns **true**

T[2 + 0] = B and P[0] = B

T[2 + 1] = A and P[1] = A

T[3 + 1] = C and P[2] = C

BAC matches BAC
#### 2.4. Naive algorithm is based on matchesAt

Naive algorithm runs |T| - |P| + 1 (i = 0, 1, 2, ..., |T| - |P| + 1) iterations. In each iterations function matchesAt is calling with p = i.

### 3. Sunday's algorithm
Sunday algorithm is based on a dictionary with |A| elements. Each letter stores the position of its last occurance in the pattern.

#### 3.1. Example (table)
*A = {A, B, C, D, E}*

*P = ACBCDA*

| A | B | C | D | E |
| - | - | - | - | - |
| 5 | 2 | 3 | 4 | -1 |

#### 3.2. Sunday's algorithm reduces the number of matchesAt calls

A = {A, B, C, D, E}

T = ACBADA

P = CB

| A | B | C | D | E |
| - | - | - | - | - |
| -1 | 1 | 0 | 0 | -1 |

p = 0 : matchesAt(T, P, i) AB != CB

**AC**BADA

**CB**

p = p + |P| # p <- 0 + 2

p = p - lastp[T[p]] # p <- 2 - 1

p = 1: matchesAt(T, P, i) CB == CB

A**CB**ADA

**CB**

p = p + |P| # <- 1 + 2

p = 3 - lastp[T[p]] # p <- 3 - (-1) 

p = 4: matchesAt(T, P, i) 

ACBA**DA**

**CB**
