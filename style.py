def btnStyle():
    return """
    QPushButton{
        /*select-background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0.5, stop: 0 black, stop: 1 white);*/
        border-style: outset;
        border-width: 2px;
        border-radius: 8px;
        border-color: black;
        font: 13px;
        padding: 4px;
        min-width: 4em;
        }
        """
def playgroundStyle():
    return """
    QWidget{
        background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: 0 #045105, stop: 1 #224923);
        }
         """

def textEditStyle():
    return """
        QTextEdit{
        background-color: black;
        border-style: outset;
        border-width: 2px;
        border-radius: 8px;
        border-color: black;
        color: #008F11;
        font: 14px Times Bold;
        padding: 2px;
        min-width: 4em;
        }
        QScrollBar{
        height: 15px;
        }
        QToolTip { 
            font: 10pt Times Bold;
            background-color: black;
            color: #008F11;
            border-style: outset;
            border-width: 2px;
            border-radius: 8px;
            border-color:  black;
            }                  
         """
def lineEditStyle():
    return """
     QLineEdit {
            font: 10pt Times Bold;
            background-color: black;
            color: #008F11;
            border-style: outset;
            border-width: 2px;
            border-radius: 8px;
            border-color:  black;
            }
            """
   


