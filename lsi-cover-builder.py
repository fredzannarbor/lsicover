import scribus
from scribus import *
import math
import argparse
import sys
print(sys.version)

# define helper functions

def applyStyle(style, story):

    '''Try to apply style to selected text. If style doesn't exist, create it.'''

    try:

        setStyle(style, story)

    except:

        createParagraphStyle(style)

        setStyle(style, story)

    return story


# initialize variables with default values
distributor = "LSI"
trimsizewidth = 8.5
trimsizeheight = 11.0
ImprintText = "Nimble Books LLC"

if haveDoc():
    setUnit = UNIT_INCHES

# sets custom colors 
defineColor("Nimble Maroon", 0, 255, 255, 141)
defineColor("Nimble Napoleonic Green", 187, 0, 200, 187)
defineColor("Nimble Blue", 255, 171, 0, 159)
defineColor("Nimble Feldgrau", 154, 102, 131, 110)
defineColor("Nimble Metallic Gold", 113, 120, 200, 51)
defineColor("Nimble Reference Red", 0, 255, 255, 0)
defineColor("USAF Blue", 100, 66, 0, 44)
# for more aviation blues see https://en.wikipedia.org/wiki/Air_Force_blue

DominantColor = "Nimble Blue"
InvertedColor = "White"



#  sets fonts and styles

BaseFont = "Baskerville Bold"

createCharStyle(name="Title 1", font=BaseFont,
                fontsize=48, features='smallcaps', fillcolor=InvertedColor)
createParagraphStyle("Title1", linespacingmode=1,
                     alignment=1, charstyle="Title 1")

createCharStyle(name="Body Text", font=BaseFont,
                fontsize=11, features='none', fillcolor=InvertedColor)
createParagraphStyle("Body Text", linespacingmode=1,
                     alignment=3, charstyle="Body Text")

createCharStyle(name="Picture Caption", font=BaseFont,
                fontsize=11, features='none', fillcolor=InvertedColor)
createParagraphStyle("Picture Caption", linespacingmode=1,
                     alignment=2, charstyle="Picture Caption")


#  gets values from the open scribus document
#  which must be a cover template file downloaded from either LSI or KDP

PageWidth, PageHeight = getPageSize()
PageWidth = float(PageWidth)

startMsg1 = "This script 1) creates necessary layers 2) moves the bar code to its own top layer"
startMsg2 = "3) creates text boxes with title info, etc. 4) creates image boxes"
startMsg3 = "5) creates spine text & rotates it into position."

startMsg = startMsg1 + startMsg2 + startMsg3

start = scribus.messageBox(
    'Cover Builder', startMsg, ICON_WARNING, BUTTON_OK)



#  uncomment if you want user to input the text box size and convert to float

""" trimsizewidth = valueDialog('trimsizewidth', 'Enter Trim Width')
trimsizewidth = float(trimsizewidth)

trimsizeheight = valueDialog('trimsizeheight', 'Enter Trim Height')
trimsizeheight = float(trimsizeheight) """

#  input the spine width
spine = scribus.valueDialog('Spine Width', 'Enter Spine Width in Inches')
spine = float(spine)

textsafety = 0.5

#  uncomment if you want to input  the text safety

#  textsafety = scribus.valueDialog('Text Safety', 'Enter Text Safety in Inches')
#  textsafety = float(textsafety)
# ungroups and deselects

distributor = valueDialog('Distributor ', 'Enter KDP or LSI')

# ask user for dominant color

DominantColor = valueDialog('Dominant Color', 'Enter Name of Dominant Color')

# uncomment if you want to ask user for the base font

#  BaseFont = valueDialog('Base Font','Enter Exact Name of Font')

# input the book title

BookTitle = valueDialog('BookTitle', 'Enter Book Title')

# input the book's subtitle

SubTitle = valueDialog('SubTitle', 'Enter SubTitle')

#  input the author's name

Byline = valueDialog('Byline', 'Enter Byline with By')

#  set up page

if distributor == "LSI":

    topLeftX = 22.75 - 2*trimsizewidth - spine - 2*0.63 - 0.7
    topLeftY = 0.375

else:  # KDP
    topLeftX = 0
    topLeftY = 0

#  calculate the fill size

fillwidth = trimsizewidth*2 + spine + 4*textsafety + 0.2
fillheight = trimsizeheight + 4*textsafety

# calculate x coordinates

leftfilledge = topLeftX
leftfronttext = topLeftX + textsafety + trimsizewidth + spine + 0.25 + 0.9

#  calculate y coordinates

filltop = topLeftY
textboxtop = topLeftY + 0.25
spinetop = topLeftY + 0.25
NimbleNtop = topLeftY + trimsizeheight - 0.25


createLayer("Fill")

# create fill box

createRect(topLeftX, topLeftY, fillwidth, fillheight, "FillBox")
setFillColor(DominantColor, "FillBox")

createLayer("FrontImage")

# create image box that covers entire front cover

createImage(leftfronttext, topLeftY, trimsizewidth + textsafety,
            trimsizeheight + textsafety, "FrontCoverImage")

#  create front text layer

createLayer("FrontText")

# create Title box

TitleBox = createText(leftfronttext, topLeftY +
                      textsafety + 0.5, trimsizewidth - textsafety, 2)

setTextColor(InvertedColor, TitleBox)
setText(BookTitle, TitleBox)
applyStyle("Title1", TitleBox)

# create Subtitle box

SubTitleBox = createText(leftfronttext, topLeftY +
                         textsafety + 2.25, trimsizewidth - textsafety, 2)
setTextColor(InvertedColor, SubTitleBox)
setText(SubTitle, SubTitleBox)
applyStyle("Title1", SubTitleBox)
setFontSize(36, SubTitleBox)


# create Picture Caption box

PicSig = createText(leftfronttext, topLeftY + textsafety +
                    3.25, trimsizewidth - textsafety, 0.5)
setText("Picture Caption Goes Here", PicSig)
setTextColor(InvertedColor, PicSig)
applyStyle("Picture Caption", PicSig)


#  create byline box

BylineBox = createText(leftfronttext, textsafety + trimsizeheight - 3.5,
                       trimsizewidth - textsafety, 1)
setTextColor(InvertedColor, BylineBox)
setText(Byline, BylineBox)
applyStyle("Title1", BylineBox)
setFontSize(22, BylineBox)


#  put Imprint on front cover

#  customize for your own values

Imprint = createText(
    leftfronttext, textsafety + trimsizeheight - 2.5, trimsizewidth - textsafety, 1)
setTextColor(InvertedColor, Imprint)
setText(ImprintText, Imprint)
applyStyle("Title1", Imprint)
setFontSize(14, Imprint)

#  create Back text  & layers

createLayer("BackText")

BackTextBox = createText(topLeftX + textsafety + .75, topLeftY + textsafety +
                         0.5, trimsizewidth - textsafety - 1, trimsizeheight - textsafety*2 - 0.5)


setTextColor(InvertedColor, BackTextBox)
setText("back text", BackTextBox)
applyStyle("Body Text", BackTextBox)
setFontSize(11, BackTextBox)

# create Spine layer & text

createLayer("Spine")

# find the spine and select it

if distributor == "LSI":
    setActiveLayer("Background")
    deselectAll()
    unGroupObject("Group9")
    selectObject("Polygon2")
    coords = getPosition("Polygon2")



# create the text that will sit on the spine and rotate its box

setActiveLayer("Spine")

SpineTitle = BookTitle

#SpineTop = createText(topLeftX + textsafety*2 + trimsizewidth + spine - .1, topLeftY + textsafety + .25, trimsizeheight - textsafety, spine)
SpineTop=createText(coords[0] + spine, coords[1]+ 0.5, trimsizeheight - textsafety, spine - .125)

setTextColor(InvertedColor, SpineTop)
setText(SpineTitle, SpineTop)
applyStyle("Title1", SpineTop)
setTextAlignment(ALIGN_LEFT, SpineTop)
setTextVerticalAlignment(ALIGNV_CENTERED, SpineTop)
setFontSize(14, SpineTop)

rotateObject(270, SpineTop)

# add Nimble N
# typographic spine logo

NimbleN = createText(coords[0], coords[1] + 10.125, 0.25, spine - .125)
setText("N", NimbleN)
setTextColor(InvertedColor, NimbleN)
setFont("Baskerville Italic", NimbleN)
setFontSize(11, NimbleN)
setTextAlignment(ALIGN_CENTERED, NimbleN)

createLayer("ISBN")

if distributor == "LSI":
    setActiveLayer("Background")
    deselectAll()
    unGroupObject("Group8")

    l = ['Polygon97', 'Polygon98', 'Polygon99']
    print("[{0}]".format(', '.join(map(str, l))))

    groupObjects(l)

    sentToLayer("ISBN", "Group10")

# create white rectangle that sits underneath standard LSI ISBN

setActiveLayer("ISBN")

createRect(coords[0] - .25, coords[1] -
           .25, 2.25, 1.5, "UnderISBN")
setFillColor("White", "UnderISBN")
setLineColor(DominantColor, "UnderISBN")
