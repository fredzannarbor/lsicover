#/usr/bin/env python
# -*- coding: utf-8 -*-

import scribus
from scribus import *
import math  

scribus.setUnit(2)



(x, y) = getPosition()

#comment these out when it is run after the big script
#createLayer("Spine")
#createLayer("ISBN")


#create boxing rectangle that sits around standard LSI ISBN


createRect(x - .25, y-.25, 2.2,1.5,"BoxAroundISBN")
setFillColor("White","BoxAroundISBN")
setLineColor("None", "BoxAroundISBN")
selectObject("BoxAroundISBN")
sentToLayer("Spine")


