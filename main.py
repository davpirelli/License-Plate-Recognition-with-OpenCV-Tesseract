import cv2
import imutils
import numpy as np
import pytesseract

# Leggi l'immagine da file
img = cv2.imread('Auto/1.png', cv2.IMREAD_COLOR)
img = cv2.resize(img, (800, 600))  # Ridimensiona l'immagine

# Converti l'immagine in scala di grigi
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 13, 40, 40)  # Riduci il rumore mantenendo i bordi

# Trova i bordi nell'immagine
edged = cv2.Canny(gray, 30, 200)

# Trova i contorni nell'immagine con il metodo RETR_TREE
contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
screenCnt = None

# Trova il contorno del rettangolo (presumibilmente la targa)
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)

    if len(approx) == 4:
        screenCnt = approx
        break

# Verifica se è stato trovato un contorno valido
if screenCnt is None:
    detected = 0
    print("Nessun contorno rilevato")
else:
    detected = 1

# Disegna il contorno trovato sull'immagine originale
if detected == 1:
    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

# Crea una maschera basata sul contorno trovato
mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

# Estrai la regione della targa dall'immagine originale
(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx+1, topy:bottomy+1]

# Esegui l'OCR sulla regione della targa
text = pytesseract.image_to_string(Cropped, config='--psm 11')
print("Riconoscimento della targa:\n")
print("Numero di targa rilevato:", text)

# Ridimensiona le immagini per mostrarle
img = cv2.resize(img, (500, 300))
Cropped = cv2.resize(Cropped, (400, 200))

# Mostra le immagini
cv2.imshow('Auto', img)
cv2.imshow('Targa Ritagliata', Cropped)

# Attendi che l'utente prema un tasto e poi chiudi le finestre
cv2.waitKey(0)
cv2.destroyAllWindows()
