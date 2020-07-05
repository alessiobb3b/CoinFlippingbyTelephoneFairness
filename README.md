# CoinFlippingbyTelephoneFairness - how it works...

## What should this program do?

So this application is an example of how fairness work on a cryptographical protocol. **Fairness** is not easy to be explained but I'll try (my try is copy a better definition found in the magic world of internet). 
*Fairness is, loosely speaking, the property of secure protocols that guarantees that either all honest parties will receive their output or no party will receive output. We know that this property can not be achieved for all functionalities unless when a majority of parties are honest*

What I've written provides you 3 different kinds of fairness.

1. **No-fairness**
2. **Blum-Fairness**
3. **RSA-fairness**

## How does it work? Short version

You have to run the *main.py* script and pass it some parameters that we'll discover in a moment. The most importatnt thing you've to remember is that you have a client instance and a server istance.
This 2 elemnts exchange messages over a TCP connection.
Our two people, Alice and Bob, will try to play a match of *coin flipping* over a phone (simulated in this case obviously). How can we garantee for both of them that the other one is not trying to cheat? 

## No-Fairness

Yeah, ehm... it is already written in the title. There is no fairness so when Bob yells at the phone to Alice his choise she will always win the match. In the script Alice will randomically flip the coin for 11 times but if Bob obtains at least 5 point, instead of flipping the coin, Alice will just say to Bob the side chosen by Alice.
Unluckily Bob will never win... poor Bob.

## Blum-Fairness

Ok, now we introduce fairness so Alice will not be able to cheat against Bob. This kind of fairness is provided us by a great mathematician named *Manuel Blum*.
If you want to understand in a more complete way his work you can read the [pubblication](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=51B5F706A8A9CE5DF3AE21FC086830E7?doi=10.1.1.453.3609&rep=rep1&type=pdf).
I'll try to explain it in a simple way.
To archive fairness we will use the **Jacobi symbol** and **Modular arithmetic**. 

<a href="https://www.codecogs.com/eqnedit.php?latex=\exists&space;\,&space;x,y&space;\in&space;Z_n^*&space;\,&space;|&space;\,&space;x^2&space;\equiv&space;y^2&space;\,&space;mod&space;\,&space;n,&space;\Bigl(\frac{x}{n}\Bigr)&space;\not\equiv&space;\Bigl(\frac{y}{n}\Bigr)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\exists&space;\,&space;x,y&space;\in&space;Z_n^*&space;\,&space;|&space;\,&space;x^2&space;\equiv&space;y^2&space;\,&space;mod&space;\,&space;n,&space;\Bigl(\frac{x}{n}\Bigr)&space;\not\equiv&space;\Bigl(\frac{y}{n}\Bigr)" title="\exists \, x,y \in Z_n^* \, | \, x^2 \equiv y^2 \, mod \, n, \Bigl(\frac{x}{n}\Bigr) \not\equiv \Bigl(\frac{y}{n}\Bigr)" /></a>

Basically we're going to build a set of numbers relatively prime to our starting number *n*. *n = p x q* where both p and q follow this rule: 

<a href="https://www.codecogs.com/eqnedit.php?latex=a&space;\in&space;\mathbb{N}&space;\,&space;|&space;\,&space;a&space;\equiv&space;3&space;\,&space;mod&space;\,&space;4" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a&space;\in&space;\mathbb{N}&space;\,&space;|&space;\,&space;a&space;\equiv&space;3&space;\,&space;mod&space;\,&space;4" title="a \in \mathbb{N} \, | \, a \equiv 3 \, mod \, 4" /></a>

Then we build <a href="https://www.codecogs.com/eqnedit.php?latex=Z_n^*" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Z_n^*" title="Z_n^*" /></a> (set of numbers relatively prime to n)


