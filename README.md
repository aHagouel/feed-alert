# feed-alert


#Background: 

Shrimp farmers employ Autofeeders -- semi-intelligent buckets with mechanical dispensers -- to give feed to hungry shrimp frequently, maximizing  opportunities for shrimp to eat and minimizing feed that's left uneaten. It's critical to ensure machines are full of feed and working properly so that the correct amount of feed is given to a pond and growth rates stay on track with harvest targtes. 

These machines have to dispense food whenever hungry shrimp are present. There are two reasons why this may not happen:
  1. The hopper has run out of food to give. Without food in the hopper, the machine can't feed the shrimp, and a hungry shrimp doesn't grow which extends cycle time. 
  2. The machine is malfunctioning -- most commonly feed gets stuck in the mechanical dispenser at the bottom of the bucket, but there can also be issues with the dispense command 
  
  
Therefore, having a clear signal of how much feed is in a specific hopper vs. how much feed is planned to be distributed can help shrimp farmers plan which machines to fill and identify silent mechanical failures.


#Problems:
- Hard to trust whether feed hoppers are full remotely. I believe they use feed distributed to calculate the status of the hopper which is inaccurate (motor being told to spin != feed actually getting to and being released from the motor. <bioFeeder screenshot of empty / full bucket being sporadic>
- Problem discovery happens when hoppers are checked manually, feed may have been full for hours, reducing feed inputted to pond and slowing growth.
- No mobile alerting, must monitor desktop all day for issues. In Ecuador, shrimp farm ponds typically have between 1.1 and 1.5 autofeeders per Ha, and ponds are around 8 Ha. Single farm organizations can have up to 40 ponds, meaning some farm teams may have to monitor working condition of over 480 machines. 


#Requirements:
So what if we built a simple way to track the fill status of a bucket-like apparatus? 

Must: 
- Notify user when a "hopper" is empty
- Deliver notification through mobile
- Be very cheap, ideally < $30 to create with DIY components

Should:
- Notify user when feed has 1 week to empty
- Not notify user when feed is being adjusted
- Be compatible with a hopper with a bottom extruder

Could:
- Calculate & show % full
- Track time-to-empty


Won't:
- Work offline, assume connection possible

#Solution
Everyone, say hi to Maui. She's not a shrimp, but she does shrimp-like things like eat on a schedule and gets really upset if she isn't fed on that schedule. If you squint, she actually looks like a shrimp, too. 

We'll use Maui's food storage bucket to simulate an autofeeder as it stores food which empties at a somewhat predictable frequency and allows us to test for some scenarios.
