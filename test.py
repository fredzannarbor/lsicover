import scribus

if scribus.haveDoc():
    nbrSelected = selectionCount()

    objList = []

    for i in range(nbrSelected):
        objList.append(getSelectedObject(i))
        
    for i in range(nbrSelected):
        try:
            obj = objList[i]
            props = ""
            propList = getPropertyNames(obj)
            for p in propList:
                try:
                    props = props + p + " (" + str(getPropertyCType(obj, p)) + "): "
                    props = props + str(getProperty(obj, p))
                except:
                    nothing = "nothing"
                props = props + "\n"
            messageBox("Property Info for " + obj, "Below is a property list for the selected object named " + obj + "\n" + props, ICON_INFORMATION)
        except WrongFrameTypeError:
            nothing = "nothing"