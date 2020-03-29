# Budget Allocation Attribution Model
Attribution model of different marketing platform to optimise the investments.

### [Dataset Source](http://ailab.criteo.com/criteo-attribution-modeling-bidding-dataset/)

## Dash Visualisation:

![Farmers Market Finder Demo](Dash-Visualisation.gif)

## Attribution Models

### 1 – First Touch Attribution Model
**What is First Click / Touch Attribution Model?**</br>
The first touch attribution model works on a straightforward formula.
When a visitor comes to your website for purchasing anything, the first medium/channel/touchpoint which the visitor uses to get to your site will get all the attributes of that sale.</br>

**How does First Click Attribution Model work?**</br>
Let suppose you have a business that deals with selling laptops and computing accessories online. Like any business, you have implemented multiple tactics such as display ads on Google, Facebook, and email outreach your list, SEO, etc.
A prospective visitor sees your Adwords ad and lands on your website for the first time. They might browse around, signup to your email newsletter, follow your Facebook page and leave.
After a few days, they come back to your website and purchases your product.
Though, they might not immediately make a purchase, and have interacted with other channels as well in the meanwhile ( email newsletter, Facebook page update), all the credit for this sale is attributed to Google Adwords, as it was the first click and interaction of your website with them.</br>

**When to use and not to use First Click Attribution Model?**
First Click Attribution Model works excellent when you are trying to identify which channel brings in the most leads or customers.
From a content marketing perspective, First Click Attribution models help you determine the best channel which is creating awareness of your content or brand.
It is also useful when you have minimal marketing channels ( such as focusing only on Facebook and Google Ads).
Similarly, First Click Attribution Model is least effective when you have multiple marketing channels as this model gives no value whatsoever to other touch points.

### 2 – Last Click Attribution Model
**What is Last Click Attribution Model?**</br>
In the last click attribution model, all credit is given to the last tactic marketing tactic/touch point after which the conversion happens.</br>

**How does Last Click Attribution Model work?**</br>
You are the owner of a mobile company and are highly active in all the key marketing channels to grab the attention of prospects looking to buy a new phone.
In all those marketing processes a customer comes to your website using Facebook ad but then goes away for any reason.
You or your marketing team would like to track and bring them back to your sales page through email campaigns, retargeting and more.
And from all the tactics the last tactic after which the prospect is converted into a customer will be given all the credit for that sale. This could be your email campaign or even a direct visit to the website by the customer.</br>

**When to use and not use the Last Click Attribution Model?**</br>
Last Click Attribution Models are very useful in understanding high impact touch points in the bottom of your funnel. They help you know which channels are driving the most conversions.
In fact, it is the go-to attribution model for analytics software like Google Analytics which gives all credit to the last touchpoint before a conversion or goal.
However, the last click attribution model obscures the other channels that played an essential role in your brand discovery and prospect nurturing. This model is also least effective for channels that require a lot of research before a prospect makes up their mind.

### 3- Linear Attribution Model

**What is Linear Attribution Model?**</br>
Linear attribution model gives the same credit to every channel across the whole sales journey. It equally divides the attribute to every single channel the customer interacted before completing a purchase.</br>

**How does Linear Attribution Model work?**</br>
A consumer sees the ad of your SaaS on Facebook and decides to visit your website by clicking the ad. Then a few days later they directly visit your site for gathering more information.
Some days later, they see you retargeted ad on a website, visit your site and then finally signup for your software.
According to the linear attribution model, the credit is divided equally among all the channels, starting from the Facebook ad till the last retargeted ad.
When to use and not to use Linear Attribution Model?
Linear attribution model works well in understanding and finding all channels that resulted in brand awareness and conversion.
They also help identify channels that are consistent in all sales journeys, especially the ones that are driving actual conversions.
However, with all of its merits, marketers often don’t use this model.
In fact, it’s a total opposite of the primary reason why attribution models are implemented, i.e. find “which channel” rather than “all channels”.
When all channels get equal credit, how can we shortlist the best among them?

### 4 – Time Decay Attribution Model
**What is the Time Decay Attribution Model?**</br>
In this attribution model, the preference is given to the channels that are extremely close to the conversion point instead of those channels through which the journey started.</br>

**How does Time Decay Attribution Model work?**</br>
Consider you own an online shoe store, and you started attracting prospects through Google Ads, without the conversion yet.
Then probably you retarget them to subscribe them to your blog and send them email campaigns around you offers.
However, all without any conversion again.
After some time the prospect stumbled on your website and purchased a shoe from you.
In this condition, the organic search traffic gets the maximum edge because it was the last channel that assisted the customer towards conversion.</br>

**When to use Time Decay Attribution Model?**</br>
Time Decay Attribution Model is useful in understanding that which channels are driving conversions. It also helps in understanding that which channel is driving which activity and let you focus your marketing budget and efforts across them.
Similar to the position based attribution model, Time Decay Attribution Models gives the least important focus on earlier channels that helped in creating awareness and demand.
For B2B, Time Decay Attribution Model might not be useful as in most cases it will give the most weight to direct channel, which usually is wrong as the prospect have to go a series of promotions and informational content before they convert.

### 5 – U-Shaped Attribution Model
**What is the U-Shaped Attribution Model?**</br>
Position based attribution model, also known as U Shaped Attribution Model, gives a certain percentage to all the channel that contributes towards a successful conversion.
The first and last channel shares 40% of credit among each of them, and the rest of the 20% is equally divided to the other channels that come in between.</br>

**How does the Position Based Attribution Model works?**</br>
A customer decides to purchase an insurance policy online and start researching this from Google. Luckily, you were on top of the list, and he/she clicks that link to get to your website.
On your site, they join your email list by downloading a brochure and then continues to read different pages of your website. Then they come back again on your website through your Facebook page in a few days.
Finally, after some days, they saw another ad of your company while using Facebook and finalizes the purchase.
In that case, the organic search and the Facebook ad will get the 40% credit each, while the rest of the channels will distribute the remaining 20% credit among them.</br>

**When to use and not to use Position Based Attribution Model works?**</br>
The position based attribution models work great for understanding which;
Channel is best for acquiring an audience
And which channel is great for conversions
After all, these are perhaps the most critical touch points every performance marketer is seeking.
The only problem with Position based attribution models is the timing and least importance given to nurturing campaigns.
For example, a visitor might first interact with you six months before and forgot. However, later, they interacted with 2-3 more of your channels before conversion.
If you are in e-commerce, it might not make sense for your customers to buy Christmas décor items in May-June, but it makes perfect sense in Nov / Dec.
Having said that the first channel might be wrongly considered influential.


# Dataset Description
#### Timestamp:</br>
timestamp of the impression (starting from 0 for the first impression). The dataset is sorted according to timestamp.
uid a unique user identifier
#### Campaign:</br>
a unique identifier for the campaign
#### Conversion:</br>
1 if there was a conversion in the 30 days after the impression (independently of whether this impression was last click or not)
#### Conversion_Timestamp:</br>
the timestamp of the conversion or -1 if no conversion was observed
#### Conversion_id:</br>
a unique identifier for each conversion (so that timelines can be reconstructed if needed). -1 if there was no conversion
#### Attribution 1: </br>
if the conversion was attributed to Criteo, 0 otherwise
### Click 1:</br>
if the impression was clicked, 0 otherwise
### Click_pos:</br> 
the position of the click before a conversion (0 for first-click)
### Click_nb:</br>
number of clicks. More than 1 if there was several clicks before a conversion
### Cost:</br>
the price paid by Criteo for this display (disclaimer: not the real price, only a transformed version of it)
### CPO(Cost per order):</br>
the cost-per-order in case of attributed conversion (disclaimer: not the real price, only a transformed version of it)
### Time_Since_Last_Click: </br>
the time since the last click (in s) for the given impression
### Cat[1-9]: </br>
contextual features associated to the display. Can be used to learn the click/conversion models. We do not disclose the meaning of these features but it is not relevant for this study. Each column is a categorical variable. In the experiments, they are mapped to a fixed dimensionality space using the Hashing Trick (see paper for reference).

