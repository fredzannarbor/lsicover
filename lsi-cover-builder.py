#/usr/bin/env python
# -*- coding: utf-8 -*-

import scribus
from scribus import *
import math
import argparse
import sys
print(sys.version)


def applyStyle(style, story):

    '''Try apply style to selected text. If style doesn't exist, create it.'''

    try:

        setStyle(style, story)

    except:

        createParagraphStyle(style)

        setStyle(style, story)

    return story

distributor = "LSI"


if haveDoc():
    setUnit = UNIT_INCHES

startMsg1 = "This module calculates spine width for LSI template then uses that info to place "
startMsg2 = "horizontal and vertical guides on the page and calculate the correct width for "
startMsg3 = "text and image boxes."

startMsg = startMsg1 + startMsg2 + startMsg3

PageWidth, PageHeight = getPageSize()
PageWidth = float(PageWidth)

start = scribus.messageBox(
    'Spine Width Calculator & Guide Applier', startMsg, ICON_WARNING, BUTTON_OK)

#sets colors (no need to import color palette any longer)

defineColor("Nimble Maroon", 0, 255, 255, 141)
defineColor("Nimble Napoleonic Green", 187, 0, 200, 187)
defineColor("Nimble Blue", 255, 171, 0, 159)
defineColor("Nimble Feldgrau", 154, 102, 131, 110)
defineColor("Nimble Metallic Gold", 113, 120, 200, 51)
defineColor("Nimble Reference Red", 0, 255, 255, 0)



createLayer("ISBN")

#ungroups and deselects

distributor = valueDialog('Distributor ', 'Enter KDP or LSI')

if distributor == "LSI":
    
    if objectExists("Group10"):
        unGroupObject("Group10")
        sentToLayer("ISBN", "Group9")

    else:
        print('no group10')

else:
    pass # no action


#ask for the top left xy

topLeftX = 3.5
topLeftY = 0.25

# topLeftX = valueDialog('topLeftX', 'Enter X coord of top left corner')
#topLeftX = float(topLeftX)

#topLeftY = valueDialog('topLeftY', 'Enter Y coord of top left corner')
#topLeftY = float(topLeftY)

#find out the dominant color

DominantColor = valueDialog('Dominant Color', 'Enter Name of Dominant Color')
InvertedColor = "White"

BaseFont = "Baskerville Bold"

createCharStyle(name="Title 1", font=BaseFont,
                fontsize=36, features='smallcaps', fillcolor=InvertedColor)
createParagraphStyle("Title1", linespacingmode=1,
                     alignment=1, charstyle="Title 1")

createCharStyle(name="Body Text", font=BaseFont,
                fontsize=11, features='none', fillcolor=InvertedColor)
createParagraphStyle("Body Text", linespacingmode=1,
                     alignment=3, charstyle="Body Text")


#find out the base font


# BaseFont = valueDialog('Base Font','Enter Exact Name of Font')

print(BaseFont)


#find out the book title

BookTitle = valueDialog('BookTitle', 'Enter Book Title')

#find out the book's subtitle

SubTitle = valueDialog('SubTitle', 'Enter SubTitle')

# find out the author's name

Byline = valueDialog('Byline', 'Enter Byline with By')


# find out the text box size and convert to float

trimsizewidth = valueDialog('trimsizewidth', 'Enter Trim Width')
trimsizewidth = float(trimsizewidth)

trimsizeheight = valueDialog('trimsizeheight', 'Enter Trim Height')
trimsizeheight = float(trimsizeheight)


# find out the spine width
spine = scribus.valueDialog('Spine Width', 'Enter Spine Width in Inches')
spine = float(spine)

#find out the textsafety

textsafety = 0.5
# textsafety = scribus.valueDialog('Text Safety', 'Enter Text Safety in Inches')
# textsafety = float(textsafety)

# calculate the fill size

fillwidth = trimsizewidth*2 + spine + 4*textsafety + 0.2
fillheight = trimsizeheight + 4*textsafety


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

createRect(topLeftX, topLeftY, fillwidth, fillheight, "FillBox")
setFillColor(DominantColor, "FillBox")

createLayer("FrontImage")

#create image box that covers entire front cover

createImage(leftfronttext, topLeftY, trimsizewidth + textsafety,
            trimsizeheight + textsafety, "FrontCoverImage")
#
# create front text layer
#
createLayer("FrontText")

#create Title box

TitleBox = createText(leftfronttext, topLeftY +
                      textsafety + 0.25, trimsizewidth - textsafety, 2)

setTextColor(InvertedColor, TitleBox)
setText(BookTitle, TitleBox)
applyStyle("Title1", TitleBox)

#create Subtitle box

SubTitleBox = createText(leftfronttext, topLeftY +
                         textsafety + 2, trimsizewidth - textsafety, 2)
setTextColor(InvertedColor, SubTitleBox)
setText(SubTitle, SubTitleBox)
applyStyle("Title1", SubTitleBox)
setFontSize(24, SubTitleBox)


#create Picture Caption box

PicSig = createText(leftfronttext, topLeftY + textsafety +
                    3, trimsizewidth - textsafety, 0.5)
setText("Picture Caption Goes Here", PicSig)
setTextColor(InvertedColor, TitleBox)
setTextAlignment(ALIGN_RIGHT, PicSig)
setFontSize(11, PicSig)
setFillColor(DominantColor, PicSig)


# create byline box

BylineBox = createText(leftfronttext, topLeftY + 5,
                       trimsizewidth - textsafety, 1)
setTextColor(InvertedColor, BylineBox)
setText(Byline, BylineBox)
applyStyle("Title1", BylineBox)
setFontSize(22, BylineBox)


# create Nimble Books logo

NimbleLogoType = createText(
    leftfronttext, textsafety + trimsizeheight - 2.5, trimsizewidth - textsafety, 1)
setTextColor(InvertedColor, NimbleLogoType)
setText("Nimble Books LLC", NimbleLogoType)
applyStyle("Title1", NimbleLogoType)
setFontSize(14, NimbleLogoType)

# create Back text layer

createLayer("BackText")


#create Back text box

BackTextBox = createText(topLeftX + textsafety, topLeftY + textsafety +
                         0.25, trimsizewidth - textsafety, trimsizeheight - textsafety*2 - 0.5)


setTextColor(InvertedColor, BackTextBox)
setText("back text", BackTextBox)
applyStyle("Body Text", BackTextBox)
setFontSize(11, BackTextBox)

#create Spine layer

createLayer("Spine")


#create the text that will sit on the spine and rotate its box

SpineTitle = BookTitle
SpineTop = createText(topLeftX + textsafety + trimsizewidth + spine,
                      topLeftY + textsafety + .25, trimsizeheight - textsafety, spine)
setTextColor(InvertedColor, SpineTop)
setText(SpineTitle, SpineTop)
applyStyle("Title1", SpineTop)
setTextAlignment(ALIGN_LEFT, SpineTop)
setFontSize(14, SpineTop)

rotateObject(270, SpineTop)

#create white rectangle that sits underneath standard LSI ISBN

createRect(topLeftX + textsafety*2, trimsizeheight -
           1.5, 2.2, 1.5, "UnderISBN")
setFillColor("White", "UnderISBN")
setLineColor(DominantColor, "UnderISBN")



