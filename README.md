# Are you an autofeeder half full or half empty kind of person?

## Summary

At xpertSea, I work to make Ecuadorian shrimp farmer's operations more productive and sustainable through technology. Recently we discovered that managing autofeeders -- semi-autonomous feeding buckets with mechanical dispensers -- is a critical task for a optimizing feed in shrimp production and farmers often rely on manual inspection of hopper fill status to identify, debug and correct issues that may result in missed feed opportunities. This is a proof of concept that it may be possible to create an automated way to detect hopper fill status using cheap hardware + IoT.


## Why does this matter at all for shrimp farmers?

Feed optimization is the bread & butter of a profitable shrimp farming operation. Shrimp farmers spend the 3 to 4 month growth cycle trying to convert every granule of human-undesirable shrimp feed into the shrimp that line the glass of that delicious shrimp cocktail you just paid $17 for. Feed is ~55% of a farmer's operating expenses, and if too much feed is given, feed is left uneaten and investments literally dissolve in the pond, degrading the water quality (& stressing the fragile shrimpies out). If too little feed is given, shrimp grow slowly and harvest cycles are extended (meaning more exposure to risk & fewer revenue opportunities in the year). To optimize, Ecuadorian shrimp farmers are shifting from manual feeding, 2x a day feeding, to implementing continuous automated feeding with Autofeeders -- semi-intelligent feeding buckets that float & dispense feed over the water -- to optimize the opportunity for shrimp to eat and minimize feed that's left uneaten.

These IoT machines are awesome and somewhat simple. They consist of a 50-150kg capacity bucket (called a hopper) attached to a frame of buoys, use a mechanical dispenser to create a feeding radius for the hungry shrimp below. A "central unit" controls and reports on the status of the connected machines and software dashboards report on machine status and allow for feeding configuration. Fun fact: more advanced autofeeders determine when and how much to feed by listening to the sound of shrimp chewing using something called a hydrophone... here's an audio file of what that sounds like for the curious <TODO>. 

Here's an autofeeder system diagram provided by [AQ1 Systems](http://www.aq1systems.com/uploaded/271/13510041_55sf200brochure_loresoct2.pdf), the team who first brough hydrophone autofeeder technology to Ecuador:
<img width="733" alt="image" src="https://user-images.githubusercontent.com/9829937/197421505-7c5cee87-41af-43e3-8c8c-384cfcb78b68.png">


When autofeeders are implemented well, the results are dramatic: >30% improvements in growth rate and >20% increases in feed conversion ratio are not uncommon vs. traditional methods. [This study](https://www.researchgate.net/publication/330566608_Automated_feeding_systems_in_pond_production_of_Pacific_white_shrimp) showed shrimp yield (lb output + value) DOUBLING when compared to traditional hand-feeding methods. Some farmers I've talked to have referred to the machines as life changing. It's therefore not surprising that shrimp farmers' adoption of these machines is skyrocketing. [eFishery](https://efishery.com/en/products/), an autofeeder + marketplace + financing company operating in Asia [raised $90m in January '22](https://techcrunch.com/2022/01/10/indonesias-efishery-raises-90m-from-temasek-softbank-vision-fund-2-and-sequoia-capital-india/) and [$30M again in October '22](https://www.seafoodsource.com/news/premium/business-finance/indonesian-start-up-efishery-secures-usd-33-million-for-expansion). Ecuadorian shrimp farmers are adopting quickly and are asking which, when, and how much instead of if. 


## So are Autofeeders just plug & play? 

Not really! We recently partnered with a farm to trial autofeeders and we quickly learned that these machines need specialized people on the farm constantly refilling, monitoring, and configuring the machines to ensure the shrimp get fed the amount they should be. 

There are three reasons why autofeeders may not distribute enough feed to the pond:
  1. Hoppers need to be constantly re-filled. Without food in the hopper, the machine can't feed the shrimp (DUH), and a hungry shrimp doesn't grow. Farm teams must ensure that there's enough feed by the pond for re-filling the next day and that feeders have sufficient feed for the upcoming feeding period. Farms sometimes offset this requirement by purchasing machines with larger feed carrying capacities.
  2. Bad configuration. After initial installation, this would typically be around feed quantity to distribute, especially as shrimp behavior changes. 
  3. Some part of the system may malfunction -- most commonly mechanical issues due to feed getting wet and clogging the mechanical dispenser or some reliabliity issues with the motors. Other issues included communication failures between the software / central units / autofeeders (internet can be really bad on these large and remote farms).
  
Managing these issues seems pretty straightforward, right? Just fill the machine and make sure the feed is going into the pond. Well, a few things make this complicated:
- **Silent failures** The software is telling you it's dispersing feed and that everything looks good but when you get to the machine the hopper is full. This typically happens with non detected mechanical failures. In our collaboration, these problems were always discovered when teams woke up to see hoppers full of feed (aka lost a day of feeding!!). These are the worst.
- **Binary & unreliable fill status** I'm not sure what the root cause is, but hopper fill status on the software was not totally reliable and only had full/empty status. Fullness (50kgs vs 10kgs left in the machine) matters a lot to farmers. Here's a view of the fill status of a hopper -- a binary empty / full signal that was sporadically on and off at times across different machines. Note the large stretches of empty hoppers that could have been feeding!
![image](https://user-images.githubusercontent.com/9829937/197882201-a0b2a3c0-093c-4f5c-a2c0-4003330a896d.png) 
- **Alerts...? Anyone?** Few brands have made autofeeder calibration notifications rock solid. When non silent failures do arise, they tend to be poll-based alerts on desktop UIs, so unless you're watching the screen all day (some people's job on the farm is literally to do that), you'll miss it. 
- **Scale** In Ecuador, it's not atypical to see a farm with 40, 8 hectare ponds (that's like 790 football fields) and farms typically have between 1.2 and 1.5 autofeeders per Ha. So, filling and ensuring over 480 machines are functioning across 790 football fields of water is definitely challenging. Some of the XL farms (think several of these large farms managed by a single organization) have "SWAT" teams dedicated to managing machines and instructing farm personell.

By the way, this is just to make sure the machines are working. There are also significant impacts to managing the water quality & increased biomass in the pond due to increased feed & growth, but we're not focusing on that here.

## What if farmers could always know how full their autofeeders are?
  
So what if we built a simple way to track the fill status of a bucket-like apparatus that floats on water? Having a clear signal of how much feed is in a specific hopper can help farmers estimate which machines will need to be refilled and when to help with feed logistics & ordering and quickly identify silent mechanical failures to prevent underfeeding. 
  
  
I'm going to focus this proof of concept on the use case of alerting when an autofeeder needs to be refilled. It's not the most valuable to a farmer, but it's the simplest one to implement and proves whether we'll be able to estimate hopper fill status. This thing...

### Must: 
- Estimate hopper fill status automatically
- Notify user when a "hopper" is empty
- Deliver notification through mobile
- Be very cheap, ideally < $30
- Be compatible with bottom-dispensing hoppers that float on water
- Work in light & dark conditions

### Should:
- Notify user when feed has 1 week to empty
- Not notify user when feed is being adjusted / filled

### Could:
- Alert when hopper has way more feed in it than expected 
- Provide a live view of hopper fill status
- Notify via WhatsApp (preferred communication protocol in Ecuador)

### Won't:
- Work offline, assume connection possible rn


## Solution
The solution is fairly straightforward: use a distance sensor strapped to the top of an autofeeder "hopper" and send WhatsApp messages based on the distance of the feed to the sensor. 

First, say hi to my dog Maui -- she's our shrimp for this project. She's not _actually_ a shrimp, but she does shrimp-like things like eat on a schedule and gets really upset if she isn't fed at the right time. If you squint, she actually looks like a shrimp, too. She's a good girl.

<img width="624" alt="image" src="https://user-images.githubusercontent.com/9829937/197424296-cb1c206c-eb54-4915-83b9-88c6b331c6a9.png">


Okay, back to the design, here it is:
  
<img width="700" alt="image" src="https://user-images.githubusercontent.com/9829937/197865130-39510d9c-4a64-45f8-82ca-5f41f9c0a22e.png">


1. Maui's food storage bucket was used to simulate an autofeeder's hopper as it stores food which empties at a somewhat predictable frequency and allows us to test for some scenarios. For those wondering, she eats Whole Hearted's Beef & Brown Rice recipe, but I should probably move to something better.

2. An [ultrasonic sensor](https://www.adafruit.com/product/3942?gclid=Cj0KCQjw166aBhDEARIsAMEyZh5hnZYPjSMhwL2mnJjwpT8mpTGLdO6UNkRYgl7pwaotRw5qHYf51pIaAuo1EALw_wcB) detects how close the feed is to the top of the bucket. I picked an ultrasonic sensor because unlike traditional silo weighting in agriculture which have their supports resting on scales, our machines float on water and adding scales to buoys seemed silly and complicated. Ultrasonic sensors work at night, seem accurate enough (farmers don't need to wait to refill or order feed when the last granule goes in), and are *super* cheap.
  
3. A wifi-enabled [Raspberry Pi Pico W]** (https://www.adafruit.com/product/5544) was used to read responses & implement simple alerting & reporting rules.

4. [Twilio](https://www.twilio.com/messaging/whatsapp) was used to test out alerting, and they had WhatsApp integration so that was great!

Ignoring the cost of the food bucket and prototype peripherals (breadboard, power source, jumper wires, etc.), the total cost of two key components was $10.95 USD before tax and shipping 🏄‍♂️

NOTE ** In the image above you I'm using a Raspberry Pi 4 because I shorted my other pi and wanted to finish the prototype.

## First E2E test + next steps
A first successufl E2E test was successful; this included measuring distance to feed pelets + detecting when I'm opening/closing the bucket + sending WhatsApp messages based on what an "empty" threshold is + a grace period to not spam the subscriber. Sorry for the PICTURE of my screen instead of a screenshot. I'm turning into my mom 😇

<img width="1033" alt="image" src="https://user-images.githubusercontent.com/9829937/197425114-55bd3a63-f2ba-4e36-84d3-7de57b823f64.png">


For the sake of prototyping I think it's safe to call it done here as we're able to read how full the hopper is and make decisions on feed fill status automatically. The immedaite next step I'd like to take is to hook this up to a [cloud-based UI that can show hopper fill status](https://github.com/aHagouel/feed-alert/issues/9) (& change everything to %s instead of cms 🤭).


## Caveats, especially if thinking of scale
- Requires manual calibration of hopper height to work
- Power source is unclear in practice
- Any interent issues b/w hopper and control unit will delay alerting
- Hacky error handling & anomoly detection don't match Ecuadorian shrimp farming practices 
- Accuracy generally untested, ultrasonic sensors aren't great with extremely uneven surfaces.


## Additional potential applications for the shrimp industry

A constant signal on hopper feed status is interesting. Adding trends and integarting farmer feed data can open up a few new more interesting use cases as well:
  
- Notifications on interesting hopper fill status (this project)
- Hopper fill status across all hoppers on a pond and farm to simplify feed fill logistics
- Forecasting hopper fill status across the farm to automate feed planning and ordering (kind of like an Amazon Dash button, but for feed)
- Creaet additional reliability data for autofeeder hardware companies

These aren't really novel -- I stumbled upon [FeedAlert](https://www.feedalert.co.uk/the-app) while looking for similar solutions and they have already implemented most of the concepts in traditional agriculture. They also toooootally used the same name as this project!! 😉



