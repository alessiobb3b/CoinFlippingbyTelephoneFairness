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

All the most important message exchanges are encrypted using a key obtained via the *Diffie-Helman algorithm*.

Basically we're going to build a set of numbers relatively prime to our starting number *n*. *n = p x q* where both p and q follow this rule: 

<a href="https://www.codecogs.com/eqnedit.php?latex=a&space;\in&space;\mathbb{N}&space;\,&space;|&space;\,&space;a&space;\equiv&space;3&space;\,&space;mod&space;\,&space;4" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a&space;\in&space;\mathbb{N}&space;\,&space;|&space;\,&space;a&space;\equiv&space;3&space;\,&space;mod&space;\,&space;4" title="a \in \mathbb{N} \, | \, a \equiv 3 \, mod \, 4" /></a>

Then we build <a href="https://www.codecogs.com/eqnedit.php?latex=Z_n^*" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Z_n^*" title="Z_n^*" /></a> (set of numbers relatively prime to n). We need this to avoid the **Jacobi Symbol** to be equal to 0. Otherwise we will not be able to obtain a 50% chance.

Now we have all we need to complete the protocol. Alice will send to Bob a sequence of numbers with the followig criteria: <a href="https://www.codecogs.com/eqnedit.php?latex=x^2&space;\,&space;mod&space;\,n&space;\,&space;|_{x&space;\,&space;\in&space;\,&space;Z_n^*}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^2&space;\,&space;mod&space;\,n&space;\,&space;|_{x&space;\,&space;\in&space;\,&space;Z_n^*}" title="x^2 \, mod \,n \, |_{x \, \in \, Z_n^*}" /></a>

So when Bob will receive the numbers sent by Alice he will not know the Jacobi symbol of that number because we have two possibile numbers, with a different symbol, that can produce that modular result. Bob now has to guess the symbol for each number sending back his answer to Alice. Alice will now deliver to Bob the real numbers and both can check the result. Who won is based on how many symbols Bob has guessed. So at the end both have still the 50% chance to win and we also provided fairness to the protocol.

## Tecnical limitation of my Blum's implementation

Trying to code this protocol was very hard for me and i needed a lot of compromises. 
1. Dimension of *n*, Blum was looking for a 160-digit numbers and i used only a 6-digit *n*, i don't have all this computational power bro.
2. Size of <a href="https://www.codecogs.com/eqnedit.php?latex=Z_n^*" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Z_n^*" title="Z_n^*" /></a>, i have been constrained to limit the size of this set to small number of elements, otherwise i would have an huge set of numbers and for all of them i should have calculated thier *Jacobi Symbol*, that's absurd. I've limited the set to only 200 elemnts, but i also needed the set to has the same numbers of elements with a *1* symbol and *-1* symbol. So in the best case the set has going to have 200 elements (100 with symbol *1* and 100 with symbol *-1*). To change this set you will need to go into both of *client.py* (line: 70) and *server.py* (line: 52) script and change the following line altering the 200 value with whatever value you want. Pay attention to the computational cost, more numbers in the set means more time spent in *Jacobi Symbol* calculation. 
```python
super(client, self).getPlayer().setMyBlum(blumFairness(3, 200, 4))
```
```python
super(server, self).getPlayer().setMyBlum(blumFairness.createFromRaw(decryptedMessage, 200, 4, True))
```
3. Number of tosses, Blum was looking for a 80-times tosses both for the *check n passage* and for the real toss. I've used only 4 tosses for checking and 11 for the real game.
4. *Jacobi Symbol*, to check if a number (*a*) has *1* as symbol you have to verify this criteria: <a href="https://www.codecogs.com/eqnedit.php?latex=k&space;\in&space;\mathbb{N}&space;\,&space;|&space;\,&space;k^2&space;\equiv&space;a&space;\,&space;mod&space;\;&space;n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k&space;\in&space;\mathbb{N}&space;\,&space;|&space;\,&space;k^2&space;\equiv&space;a&space;\,&space;mod&space;\;&space;n" title="k \in \mathbb{N} \, | \, k^2 \equiv a \, mod \; n" /></a>. The range of *k* has been set by be to in the interval: <a href="https://www.codecogs.com/eqnedit.php?latex=k&space;\in&space;[0,n^2]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k&space;\in&space;[0,n^2]" title="k \in [0,n^2]" /></a>.
4. Execution time, i've used the *Euclide algorithm* to find the elements in the Relatively primes to n set. It has, in the worst case, a computational cost <a href="https://www.codecogs.com/eqnedit.php?latex=O(n^2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?O(n^2)" title="O(n^2)" /></a>. Besides to find the *Jacobi Symbol* you will have to wait, still in the worst case, that the program scans all the numbers between 0 and *n squared*. This means, eventually, you're gonna need some extra minutes to let this to finish...

## RSA-Fairness

The last one is a my personal revisitation of the Blum fairness. It's an easier way to archieve fairness in the coin flipping protocol. As first step Bob and Alice are both going to generate their *RSA keys* and store them into a Certification Authority (a simple web server stored on a Raspberry for example). Then Bob will send his choise to Alice using the folliwng method: <a href="https://www.codecogs.com/eqnedit.php?latex=K_b^&plus;(H(choise)))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?K_b^&plus;(H(choise)))" title="K_b^+(H(choise)))" /></a>.
Alice will now send her tosses in the same way:  <a href="https://www.codecogs.com/eqnedit.php?latex=K_a^&plus;(H(choise)))" target="_blank"><img src="https://latex.codecogs.com/gif.latex?K_a^&plus;(H(tosses)))" title="K_a^+(H(tosses)))" /></a>.
At this point Bob and Alice will exchange between them their public keys and check their validity on the CA. If both of them are valid now they can exchange the real values. To do that they will send the values encryoted only with the public jey of the other one. Bob will send:  <a href="https://www.codecogs.com/eqnedit.php?latex=K_a^&plus;(choise)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?K_a^&plus;(choise)" title="K_a^+(choise)" /></a>.
Alice will send:  <a href="https://www.codecogs.com/eqnedit.php?latex=K_b^&plus;(tosses)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?K_b^&plus;(tosses)" title="K_b^+(tosses)" /></a>

So now Bob adn Alice are able to look at the real values chosen and check if the hash function of the received value is the same of the first one. If they're not the same then the other player has tried to cheat. As hash function i've used *SHA-1* but you can change it and use whatever you want mate.

## How it works - a little bit better

To run this script you will need a *python 3* compiler and maybe more then one pc. 
The application allows you to use the following flags:
-c, this sets the program to run in client mode. You will have to launch the server instance before the client one obviously.
-s, this sets the program to run in server mode, this cannot be used with the *-c* flag.
-a, this is used to set the other player IP address. You can use your loopback IP if you want to run it in your local machine.
-ht, this allows you to choose between head or tail. It's not possible to use this for the server instance and it is not valid for the Blum option because it uses only the guessings.
To run the program you have to write this line in the terminal: 
```bash
user@opDistro:~$ python3 main.py -s -a 127.0.0.1
```
