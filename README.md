
# Congressional Gift Travel Data 
~~If you're like me, you hate xml files, and don't understand why people use them. There's probably somebody out there who does, but it's not me.~~ Anyways, this morning I went to a dope NICAR session that mentioned Congressional Gift Travel data, which is only published in an xml. So, I wrote this code to port the data into a csv. It's not perfect because the senate one currently puts multiple trips for the same employee in the same row sequentially, but it should make the data slightly more manageable. Included are the python scripts and csv files, which are current as of 3/10/2018.
### Notes about the data
The house data is much nicer, and I love it a lot. But the senate data is nasty. For starters, the only real info it gives you is when an employee or senator traveled, and when they filed. To find who sponsored their travel, you'll have to search for them specifically [here](https://soprweb.senate.gov/giftrule/) and then look at the pdf. Gross.

I've also added columns for month of travel AND ISO country codes for the travel destinations, and I've cleaned all the data in the house_total_cleaned file, making it way better for analysis. COMING SOON: a column with the coords of every travel, so you can make maps.
## How to run this data
Download the [house data](http://clerk.house.gov/public_disc/gifttravel.aspx) and the [senate data](http://soprweb.senate.gov/giftrule/giftruledownload/giftruledata.zip) and then run the scripts in the same folder as the extracted xml files.
## How to make these scripts better
The python scripts are already perfect, but if you want to contribute to my little bit of analysis in R, feel free. Right now I'm looking for a good way to get coordinates of cities.
# TIL you can open xml files in Excel
Yeah, you should probably just open it in excel and save as a csv. I suppose this was a good lesson in data scraping anyways.
