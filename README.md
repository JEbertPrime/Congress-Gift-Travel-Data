# TIL you can open xml files in Excel
Yeah, you should probably just open it in excel and save as a csv. I suppose this was a good lesson in data scraping anyways.
# Congressional Gift Travel Data 
~~If you're like me, you hate xml files, and don't understand why people use them. There's probably somebody out there who does, but it's not me.~~ Anyways, this morning I went to a dope NICAR session that mentioned Congressional Gift Travel data, which is only published in an xml. So, I wrote this code to port the data into a csv. It's not perfect because the senate one currently puts multiple trips for the same employee in the same row sequentially, but it should make the data slightly more manageable. Included are the python scripts and csv files, which are current as of 3/10/2018.
### Notes about the data
The house data is much nicer, and I love it a lot. But the senate data is nasty. For starters, the only real info it gives you is when an employee or senator traveled, and when they filed. To find who sponsored their travel, you'll have to search for them specifically [here](https://soprweb.senate.gov/giftrule/) and then look at the pdf. Gross.
## How to run this data
Download the [house data](http://clerk.house.gov/public_disc/gifttravel.aspx) and the [senate data](http://soprweb.senate.gov/giftrule/giftruledownload/giftruledata.zip) and then run the scripts in the same folder as the extracted xml files.
## How to make these scripts better
~~Maybe make the senate scraper output each distinct instance of travel in its own row, but still with the name info for the employee traveling.~~ Just use excel
