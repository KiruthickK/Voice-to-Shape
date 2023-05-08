import VoiceRecognition as VR
import DrawShapes as DS
import SpeechCommandDatasets as SCMD
import VoiceOutput as VC
VC.speech("Say a shape to draw. Say Clear to clear the screen. Say done to exit the program")
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
    elif(text in SCMD.Indianflag):
        DS.IndianFlag()
    elif(text in SCMD.directionChange):
        VC.speech("Tell me the directionm to change")
        while(True):
            text = VR.SpeechToText()
            if(text is None):
                continue
            if(text in SCMD.Direction):
                DS.ChangeDirection(text)
                VC.speech("Direction changed")
                break
            else:
                VC.speech("please provide me the valid direction")
    elif(text in SCMD.StraightLine):
        direction = ""
        distance = 0
        VC.speech("Tell me the direction")
        while(True):
            text = VR.SpeechToText()
            if(text is None):
                continue
            if(text in SCMD.Direction):
                direction = text
                break
            else:
                VC.speech("please provide me the valid direction")
        while(True):
            VC.speech("Tell the distance")
            text = VR.SpeechToText()
            if text is None:
                continue
            if text.isdigit():
                distance = int(text)
                break
            else:
                VC.speech("Please provide a valid integer as distance")
        DS.StraightLine(distance,direction)
    else:
        VC.speech("Simply waste, nothing worthy received!, i mean command")