library(lubridate)
library(geonames)
library(countrycode)
library(tidyverse)
data<- read.csv("house_total_cleaned.csv")
#Keeping the amendments can complicate some of the analysis. All the amendments are preserved in the original file.
#This line filters them out.
data<-data[data$Filing.Type != "Amendment",]

#Adding some columns for the month, so we can see what time of year members travel the most during.
data$return_month<-month(data$Return.Date)
data$departure_month<-month(data$Departure.Date)

#These lines first create separate rows for city and country, converting all state codes to USA,
#and then convert all country names to ISO abbreviations.
#The only entries that don't have the proper country abbreviations are ones for Kosovo,
#since it is not yet recognized by ISO. If a value is blank, it's Kosovo.
data$destination_country<- substring(data$Destination, regexpr(",",data$Destination) + 1 )
data$destination_country[nchar(data$destination_country)<=3]<-"USA"
data$destination_country<-countrycode(data$destination_country, 'country.name', 'iso3c')
data$destination_city<-substring(data$Destination, 0, regexpr(",",data$Destination)-1)

