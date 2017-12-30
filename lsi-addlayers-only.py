#!/usr/bin/env python

'''
A script to add new named layers to a template for an 8 x 10 LSI page.
Requires an existing document, but can be modified to
create a new document if it does not exist.

uses (See the API in Help->Scribus Manual->For Developers->Scripter API;
 haveDoc
 createLayer
 getActiveLayer
 setActiveLayer
 createText
 setUnit
 setText
 setTextColor
 setFontSize
 rotateObject

'''

from scribus import *

if haveDoc():
    setUnit=UNIT_INCHES
    defineColor("NimbleBlue",255,171,0,158)
    defineColor("NapoleonicGreen",187,0,199,186)

createLayer("Fill")
createLayer("FrontText")
createLayer("BackText")
createLayer("FrontImage")
createLayer("BackImage")
createLayer("Spine")

#create Spine top text
#   	createText(7.6,0.3,1.5,0.5,"SpineTop")
    # 	setFont("LTC Italian Old Style Regular","SpineTop")
    # 	setTextColor("White","SpineTop")
#  	setFontSize(11,"SpineTop")
#   	setTextAlignment(ALIGN_LEFT,"SpineTop")
#   	setText("Author and Short Title","SpineTop")
#  	rotateObject(270,"SpineTop")

createLayer("ISBN")
#for 6 x 9 pages
#create fill
    #createRect(1.47,0,12.5,9.25,"CoverFill")
    #setFillColor("NimbleBlue","CoverFill")

#create image box in middle of front cover
    #createImage(7.93,2.33,5.75,3.5,"FrontCoverImage")

#create Title box
    #createText(7.93,0.23,5.75,2,"Title")
    #setTextColor("White","Title")
    #setFont("LTC Italian Old Style Regular","Title")
    #setFontSize(44,"Title")
    #setTextAlignment(ALIGN_CENTERED,"Title")
    #setText("Title Text","Title")
# create Subtitle box
    #createText(7.93,2.23,5.75,2,"Subtitle")
    #setTextColor("White","Subtitle")
    #setFont("LTC Italian Old Style Regular","Subtitle")
    #setFontSize(32,"Subtitle")
    #setTextAlignment(ALIGN_CENTERED,"Subtitle")
    #setText("Subtitle Text","Subtitle")
# create byline box
    #createText(7.93,6.23,5.75,2,"Byline")
    #setFont("LTC Italian Old Style Regular","Byline")
    #setTextColor("White","Byline")
    #setFontSize(32,"Byline")
    #setTextAlignment(ALIGN_CENTERED,"Byline")
    #setText("By Author Name","Byline")
# create Nimble Books logo
    #createText(7.93,7.23,5.75,0.5,"NimbleLogo")
    #setFont("LTC Italian Old Style Regular","NimbleLogo")
    #setTextColor("White","NimbleLogo")
    #setFontSize(14,"NimbleLogo")
    #setTextAlignment(ALIGN_CENTERED,"NimbleLogo")
    #setText("Nimble Books LLC","NimbleLogo")
    #createLayer("BackText")
#create Back text box
   # createText(1.72,0.23,5.75,6,"Backtext")
    #setTextColor("White","Backtext")
   # setFont("LTC Italian Old Style Regular","Backtext")
   # setFontSize(11,"Backtext")
   # setTextAlignment(ALIGN_LEFT,"Backtext")
   # setText("paras go here","Backtext")
#create Spine


#create white rectangle that sits underneath standard LSI ISBN
   # createRect(3.72,7.23,2.2,1.493,"UnderISBN")
   # setFillColor("White","UnderISBN")
#create ISBN layer
