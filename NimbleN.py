#/usr/bin/env python
# -*- coding: utf-8 -*-

import scribus
from scribus import *

NimbleLogoType = createText(leftfronttext,10,textboxwidth,1)
setText("Nimble Books LLC", NimbleLogoType)
setTextAlignment(ALIGN_CENTERED, NimbleLogoType)
setTextColor(InvertedColor, NimbleLogoType)
setFillColor(DominantColor, NimbleLogoType)
setFontSize(14,NimbleLogoType)
