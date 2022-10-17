# Are you an autofeeder half full or half empty kind of person?

## Summary

At xpertSea, I work to make Ecuadorian shrimp farmer's operations more productive and sustainable through technology. Recently we discovered that managing autofeeders -- semi-autonomous feeding buckets with mechanical dispensers -- is a critical task for a optimizing shrimp production and farmers rely on manual inspection of hopper fill status to debug and correct issues that may result in missed feed opportunities. This is a proof of concept that it may be possible to create more reliable alerting on hopper fill status using cheap hardware + iot.


## Why does this matter at all for shrimp farmers?

Feed optimization is the bread & butter of a profitable shrimp farming operation. Every Kg of feed that is put into a shrimp pond costs farmers $, and in the course of 3-4 months, helps shrimp grow into that delicious shrimp cocktail you just paid $17 for. In the last 5 years, Ecuadorian shrimp farmers have shifted from manual feeding to using Autofeeders -- semi-intelligent feeding buckets with mechanical dispensers -- to feed hungry shrimp frequently, maximizing opportunities for shrimp to eat and minimizing feed that's left uneaten. Failure to feed shrimp optimally wastes feed and detriments water quality (feed can dissolve if too much is given) and can extends shrimp growth cycles (a.k.a. more risk exposure & fewer revenue opportunities in the year). 

These machines are awesome and somewhat simple. They consist of a big bucket that holds anywhere from 50 to 300 <TODO: verify> kgs of feed, floats on top of the water, and uses a mechanical dispenser to create a feed blast radius for some hungry shrimp. A "central unit" controls and reports on the status of ~4 machines, and often softwares report on status and allow for config. Fun fact: more advanced autofeeders determine when and how much to feed by listening to the sound of shrimp chewing using something called a hydrophone. here's an audio file of what that sounds like for the curious.

When they work well, the results are dramatic. <TODO: stats> . Some farmers I've talked to have referred to the machines as life changing. <TODO: Sales / growth estimates of autofeeders>. 


## So are Autofeeders perfect and easy to use? 

I wish, but not always. Our company recently partnered with a farm in Ecuador to bring autofeeders to the farm and we quickly learned that the machines need someone on the farm configuring, monitoring, and refilling the machines on a daily basis to ensure the shrimp were being fed the amount they should be.

We saw two main reasons that made dispensing feed from autofeeders difficult:
  1. Hopper needs to be constantly re-filled. Without food in the hopper, the machine can't feed the shrimp, and a hungry shrimp doesn't grow which extends cycle time (DUH.) Every day, the farm must ensure enough feed is by the side of the pond so that workers top the machines off. Farms sometimes offset this requirement by purchasing machines with larger feed carrying capacities.
  2. Some part of the system tend to malfunction -- most commonly mechanical issues due to feed getting wet and clogging the mechanical dispenser or some reliabliity issues with the motors. Other issues included communication failures between the software / central units / the autofeeders (internet can be really bad on these large and remote farms).
  
Managing these issues seem pretty straightforward, right? Just fill the machine and make sure the feed is going into the pond. Well, a few things make this complicated:
- _Silent failures_ The software is telling you it's dispersing feed and that everything looks good but when you get to the machine the hopper is full. This happens when a mechanical issue (like feed clogged up) happens and the software reports on what the autofeeder was told to do, but the case is not actually verifiable. These are the worst.
- _Manual inspection required_ I'm not sure what the root cause is, but hopper fill status on the software was just not accurate with the brand we were using. Here's a view of the fill status of a hopper -- a binary empty / full signal that was sporadically on and off throghout the day. <TODO: Screenshot>. In our collaboration, these problems were always discovered when the teams woke up the next day and went to the pond to see that the hoppers were full of feed (aka lost a day of feeding!!). 
- _Alerts...? Anyone?_ Few brands have optimized for the "autofeeder calibration" role on the farm. When issues arise, they appear on desktop UIs with no alerts, so unless you're watching the screen all day (some people's job on the farm is literally this), you'll miss it. 
- _Scale_ In Ecuador, it's not atypical to see a farm with 40, 8 hectare ponds (that's like 790 football fields) and farms typically have between 1.2 and 1.5 autofeeders per Ha. So, filling and ensuring over 480 machines are functioning across 790 football fields of water is definitely challenging. Some of the XL farms (think several of these Large farms managed by an organization) have "SWAT" teams for managing machiens and instructing farm personell.


## What if we could always know how full an autofeeer was?
  
So what if we built a simple way to track the fill status of a bucket-like apparatus that floats on water? Having a clear signal of how much feed is in a specific hopper vs. how much feed is planned to be distributed can help shrimp farmers plan which machines will require topping off and quickly identify silent mechanical failures. This thing...

### Must: 
- Notify user when a "hopper" is empty
- Deliver notification through mobile
- Be very cheap, ideally < $30
- Be compatible with bottom-dispensing hoppers that float on water
- Work in light & dark conditions

### Should:
- Notify user when feed has 1 week to empty
- Not notify user when feed is being adjusted / filled

### Could:
- Calculate & track % full over time
- Notify via WhatsApp (preferred communication protocol in Ecuador)

### Won't:
- Work offline, assume connection possible rn


## Solution
The solution is fairly straightforward: use a distance sensor strapped to the top of a fake autofeeder hopper and send WhatsApp messages based on the distance of the feed to the sensor. 

But first, say hi to Maui -- she's our shrimp for this project. She's not _actually_ a shrimp, but she does shrimp-like things like eat on a schedule and gets really upset if she isn't fed at the right time. If you squint, she actually looks like a shrimp, too. 


She's a good girl. Okay, back to the design, here it is:

1. Maui's food storage bucket was used to simulate an autofeeder's hopper as it stores food which empties at a somewhat predictable frequency and allows us to test for some scenarios. For those wondering, she eats <feed type>, but am open to other suggestions.

2. I used a wifi-enabled [Raspberry Pi Pico W](https://www.adafruit.com/product/5544) to read responses on an ongoing basis from 

3. An [ultrasonic sensor](https://www.adafruit.com/product/3942?gclid=Cj0KCQjw166aBhDEARIsAMEyZh5hnZYPjSMhwL2mnJjwpT8mpTGLdO6UNkRYgl7pwaotRw5qHYf51pIaAuo1EALw_wcB) to make this work. I picked an ultrasonic sensor because unlike traditional silo weighting in agriculture, our machines float on water and that seemed silly. Ultrasonic sensors work at night, are accurate enough (farmers don't need to wait to refill when the last granule goes in), and are super cheap.

Ignoring the cost of the food bucket and prototype peripherals (breadboard, power source, jumper wires, etc.), the total cost of two key components was $10.95 USD before tax 🏄‍♂️.

## Results
<TODO monday>


# Caveats, especially if thinking of scale
- Requires manual calibration of hopper height to work
- Power source is unclear 
- Interent issues will delay alerting
- Hacky error handling in my code, was just a proof of concept


# Additional potential applications for shrimp farmers
I got a lot of the below ideas when I stumbled on [FeedAlert](https://www.feedalert.co.uk/the-app) while looking for similar solutions. They also toooootally used the same name as this project!! 😉:
- Notifications (this project)
- Forecasts across all hoppers (to coordinate logistics)
- Feed ordering (kind of like an Amazon Dash button, but for feed)
- History (for managers)
- Reliability data (for autofeeder companies)






