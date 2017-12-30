#/usr/bin/env python
# -*- coding: utf-8 -*-

import scribus
from scribus import *
import math  


scribus.setUnit(2)

#set global variables

#import style file

#loadStylesFromFile("filename")

startMsg1 = "This module calculates spine width for LSI template then uses that info to place "
startMsg2 = "horizontal and vertical guides on the page and calculate the correct width for"
startMsg3 = "text and image boxes."

startMsg = startMsg1 + startMsg2 + startMsg3

PageWidth, PageHeight = getPageSize()
PageWidth = float(PageWidth)

start = scribus.messageBox('Spine Width Calculator & Guide Applier', startMsg, ICON_WARNING, BUTTON_OK)

#sets colors (no need to import color palette any longer)

defineColor("Nimble Maroon", 0, 255, 255, 141 )
defineColor("Nimble Napoleonic Green", 187, 0, 200, 187 ) 
defineColor("Nimble Blue", 255, 171, 0, 159 ) 
defineColor("Nimble Feldgrau", 154, 102, 131, 110 ) 
defineColor("Nimble Metallic Gold", 113, 120, 200, 51 ) 
defineColor("Nimble Reference Red", 0, 255, 255, 0)

#check whether there is Group 1, if not skip

#ungroups and deselects
# unGroupObject("Group1")
# deselectAll()

#get the position of the selected object
(topLeftX, topLeftY) = getPosition()
topLeftX = float(topLeftX)
topLeftY = float(topLeftY)
#positionMsg = topLeftX, topLeftY


#ask for the top left xy

#topLeftX = valueDialog('topLeftX', 'Enter X coord of top left corner')
#topLeftX  = float(topLeftX)

#topLeftY = valueDialog('topLeftY', 'Enter Y coord of top left corner')
#topLeftY = float(topLeftY)

#find out the dominant color

DominantColor = valueDialog('Dominant Color','Enter Name of Dominant Color')
InvertedColor = "White"

#find out the base font

#"Adobe Jenson Pro Regular" = valueDialog('Base Font','Enter Exact Name of Font')

#find out the book title

BookTitle = valueDialog('BookTitle','Enter Book Title')

#find out the book's subtitle

SubTitle = valueDialog('SubTitle','Enter SubTitle')

# find out the author's name

Byline = valueDialog('Byline','Enter Byline with By')


# find out the text box size and convert to float

trimsizewidth = valueDialog('trimsizewidth', 'Enter Trim Width')
trimsizewidth = float(trimsizewidth)

trimsizeheight = valueDialog('trimsizeheight', 'Enter Trim Height')
trimsizeheight = float(trimsizeheight)


# find out the spine width
spine = scribus.valueDialog('Spine Width','Enter Spine Width in Inches')
spine = float(spine)

#find out the textsafety

textsafety = scribus.valueDialog('Text Safety', 'Enter Text Safety in Inches')
textsafety = float(textsafety)

# calculate the fill size

fillwidth = trimsizewidth*2 + spine + 2*textsafety + 0.2
fillheight = trimsizeheight + 2*textsafety


#calculate x coordinates


leftfilledge = topLeftX
leftfronttext = topLeftX + textsafety + trimsizewidth + spine + 0.25

# calculate y coordinates

filltop = topLeftY
textboxtop = topLeftY + 0.25
spinetop = topLeftY + 0.25
NimbleNtop = topLeftY + trimsizeheight - 0.25

#
createLayer("Fill")
#
#create fill box
#
#fill box is now in correct location and size
createRect(topLeftX,topLeftY,fillwidth, fillheight, "FillBox")
setFillColor(DominantColor,"FillBox")
#
createLayer("FrontImage")

#create image box that covers entire front cover

createImage(leftfronttext,topLeftY,trimsizewidth + textsafety,trimsizeheight + textsafety,"FrontCoverImage")
#
# create front text layer
#
createLayer("FrontText")

#create Title box

TitleBox = createText(leftfronttext,topLeftY + textsafety + 0.25,trimsizewidth - textsafety,2)
setText(BookTitle, TitleBox)
setTextColor(InvertedColor, TitleBox)
setTextAlignment(ALIGN_CENTERED, TitleBox)
setFontSize(36,TitleBox)
setFillColor(DominantColor, TitleBox)
#

#create Subtitle box

SubtitleBox = createText(leftfronttext,topLeftY + textsafety + 2, trimsizewidth - textsafety,2)
setText(SubTitle, SubtitleBox)
setTextColor(InvertedColor, SubtitleBox)
setTextAlignment(ALIGN_CENTERED, SubtitleBox)
setFontSize(36,SubtitleBox)
setFillColor(DominantColor, SubtitleBox)
#

#create Picture Signature box
PicSig  = createText(leftfronttext,topLeftY + textsafety + 3,trimsizewidth - textsafety,0.5)
setText("Picture Signature Goes Here",PicSig)

setTextAlignment(ALIGN_RIGHT,PicSig)
setFontSize(11,PicSig)
setFillColor(DominantColor,PicSig)

#
# create byline box
BylineBox = createText(leftfronttext,topLeftY + 5,trimsizewidth - textsafety,1)
setText(Byline, BylineBox)
setTextColor(InvertedColor,BylineBox)
setTextAlignment(scribus.ALIGN_CENTERED,BylineBox)
setFontSize(22,BylineBox)
setFillColor(DominantColor,BylineBox)


# create Nimble Books logo

NimbleLogoType = createText(leftfronttext,textsafety + trimsizeheight - 2.5,trimsizewidth - textsafety,1)
setText("Nimble Books LLC", NimbleLogoType)
setTextAlignment(ALIGN_CENTERED, NimbleLogoType)
setTextColor(InvertedColor, NimbleLogoType)
setFillColor(DominantColor, NimbleLogoType)
setFontSize(14,NimbleLogoType)

# create Back text layer

createLayer("BackText")


#create Back text box

BackTextBox= createText(topLeftX + textsafety, topLeftY + textsafety + 0.25,trimsizewidth - textsafety,trimsizeheight - textsafety*2 - 0.5)
setText("back text",BackTextBox)
setTextColor(InvertedColor,BackTextBox)
setTextAlignment(ALIGN_LEFT,BackTextBox)
setFontSize(11,BackTextBox)
setFillColor(DominantColor,BackTextBox)

#create Spine layer

createLayer("Spine")


#create the text that will sit on the spine and rotate its box

SpineTitle = BookTitle
SpineTop  = createText(topLeftX + textsafety + trimsizewidth + spine,topLeftY + textsafety + .25,trimsizeheight -textsafety,spine)
setText(SpineTitle,SpineTop)
setTextColor(InvertedColor,SpineTop)
setTextAlignment(ALIGN_LEFT,SpineTop)
setFontSize(14,SpineTop)
setFillColor(DominantColor,SpineTop)

rotateObject(270,SpineTop)

#create white rectangle that sits underneath standard LSI ISBN

createRect(topLeftX + textsafety*2,trimsizeheight - 1.5,2.2,1.5,"UnderISBN")
setFillColor("White","UnderISBN")
setLineColor(DominantColor, "UnderISBN")

#create NimbleN

#create ISBN layer

createLayer("ISBN")

