
import cv2    #Laden der Bibiothek
 
filename = "example.png"  #Pfad zum Bild zuweisen
 
image = cv2.imread(filename,0)  #Bild Laden
if image is None:               #Prüfen ob das öffnen geklapt hat
    print("Unable to open " + filename)
    exit(-1)
 
cv2.imshow("An example image", image)    #Bild anzeigen
cv2.waitKey(0)
cv2.destroyAllWindows()
