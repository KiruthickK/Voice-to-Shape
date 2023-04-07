import VoiceRecognition as VR
import DrawShapes as DS
import SpeechCommandDatasets as SCMD
while(True):
    text = VR.SpeechToText()
    if(text is None):
        continue
    elif(text in SCMD.done):
        break
    elif(text in SCMD.circle):
        DS.DrawCircle()
    elif(text in SCMD.tangentCircle):
        DS.TangentCircle()
    elif(text in SCMD.clear):
        DS.ClearDrawings()
    else:
        print("Hai")

