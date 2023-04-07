import VoiceRecognition as VR
import DrawShapes as DS
import SpeechCommandDatasets as SCMD
while(True):
    text = VR.SpeechToText()
    if(text is None):
        continue
    text = text.lower()
    if(text in SCMD.done):
        break
    elif(text in SCMD.circle):
        DS.DrawCircle()
    elif(text in SCMD.tangentCircle):
        DS.TangentCircle()
    elif(text in SCMD.turtleStar):
        DS.TurtleStar()
    elif(text in SCMD.box):
        DS.Square()
    elif(text in SCMD.clear):
        DS.ClearDrawings()
    elif(text in SCMD.StraightLine):
        direction = ""
        distance = 0
        while(True):
            print("Tell the direction")
            text = VR.SpeechToText()
            if(text is None):
                continue
            if(text in SCMD.Direction):
                direction = text
                break
            else:
                print("please provide the direction")
        while(True):
            print("Tell the distance")
            text = VR.SpeechToText()
            if text is None:
                continue
            if text.isdigit():
                distance = int(text)
                break
            else:
                print("Please provide a valid integer as distance")
        DS.StraightLine(distance,direction)
    else:
        print("Simply waste, nothing received!")