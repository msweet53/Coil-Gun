## 5/12/21
### Milestone: Battery vs. Power Supply vs. Capacitor


Today we did a little testing regarding whether we wanted to use a battery or a capacitor to power the coils we are using to propel the steel object. When testing our 4 
capacitor bank charged to 36v, we found that it performed less well than our 3x 12v Pb battery series (36v). Our theory as to why this is the case is that the buildup is important 
in gaining as much speed as possible, which is why the battery performed better, because it didn’t release all its energy at once. It’s important to keep in mind that the battery 
was also probably causing the piece of steel to oscillate more due the current being steady and when the current stopped depended on how long the connection was made. Despite this, 
the steel rod still shot out of the other end more quickly.  In conclusion we have decided that we are going to stop using our capacitor bank, and start using only our battery 
bank. It is also important to keep in mind that we were using the batteries to charge the capacitor in this test. Some more advantages to using the batteries would be that it's 
more cost effective, and makes the entirety of the project much less complicated due to the fact that we won't have to set up a separate charging circuit for the capacitors as 
well. Due to the capacitors not needing to be charged, this will result in semi-automatic fire being possible in the future. 

Ideas for the future - Max S.
While I was thinking a little about this project in my free time, I had the idea of the possibility of an assisted coil gun of some sort. During the Buford Summer Engineering 
Academy I got some experience with a similar mechanism to what we are attempting to make right now, and I noticed a large difference between when I just let it start on its own 
and when I gave it a decent push with my finger. I was thinking that it might be possible to have an air assisted coil gun, where it would function as a hybrid between a coil gun 
and an air gun. One concern about this that I have is that I don't have that much knowledge about the way air pressure works, so I’m concerned that when the coils begin to speed 
up the projectile, it may end up being fast enough to pull a vacuum in the chamber slowing down the projectile. 

## 5/13/21
Today we are going to be coding the relay. Nevermind we ended up sanding the photointerrupters and getting them level with each other. The test did not yield any results unfortunately, but we know the relay works.

## 5/19/21
Today we are continuing to code the relay. Last time we worked on this we found a perfect copper piece to wrap the wire around, which is just the right size for the half inch piece of steel to fit inside. We also set up photointerrupters on our temporary coil to work with the relay that we couldn’t get working. The photointerrupters unfortunately didn’t work, so today we will test ones that have not been separated, using the same code that we were using to test the separated ones. So far the photo interrupter testing has not gone well. We have definitely wired it correctly, but the code does not yield the right results. We popped the LED in one photo interrupter because of a lack of a resistor. We finally figured out what was wrong with the code. We hadn’t been running it on the code.py file. We got the code working, but are still struggling with wiring.

## 5/20/21
### Milestone: Finishing our first photo interrupter + relay test
Today we finally managed to both wire the photo interrupter to the coil and get it working, as well as wiring the relay and get it working. We were able to develop code to make these things work in tandem with each other, and now when the interrupter is interrupted it will set off the relay. We did break a lot of photo interrupters in the process but it feels good to finally get it working. The code we developed today is pictured below.

## 5/26/21
### Milestone: Completed 36v single stage trigger enabled projectile launch
Today we finished our extremely janky prototype of a single stage 36v coil launcher. The janky test rig is trigger controlled, meaning that when you press the button the projectile is launched. We had some very promising results with the projectile moving fairly fast givin that this is only a third of the volatage we would like to use and a fifth of th stages we would like to use. I am sure that in the future when our connections arent just alligator clips and held in place, and when our photointerruptor isn't dangly and hot glued on we will have better results. 

## 5/27/21
Today we rewired our test bench for cleaness and organizational purposes. 
