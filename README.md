# License Plate Recognition with OpenCV and Tesseract
Questo script python si occupa di processare un immagine con OpenCV, cercare una targa, ritagliarla ed estrarre il testo grazie a Tesseract.

## Screenshot di esempio
<img width="612" alt="tesseract" src="https://github.com/davpirelli/License-Plate-Recognition-with-OpenCV-Tesseract/assets/6840116/2efaa18d-190d-41bd-8913-fcfaed2b6d93">

### Importazione delle Librerie
Il codice inizia importando le librerie necessarie per il riconoscimento della targa veicolo, tra cui OpenCV per l'elaborazione delle immagini, imutils per semplificare alcune operazioni, NumPy per la manipolazione di array e PyTesseract per l'OCR.

### Caricamento e Preprocessamento dell'Immagine
L'immagine del veicolo viene letta da file e ridimensionata a 800x600 pixel. Successivamente, viene convertita in scala di grigi e applicato un filtro bilaterale per ridurre il rumore mantenendo i bordi.

### Ricerca dei Contorni
Utilizzando l'algoritmo di rilevamento dei bordi di Canny, vengono individuati i contorni nell'immagine preprocessata. I 10 contorni più grandi vengono estratti e ordinati per area.

### Identificazione del Contorno della Targa
Attraverso l'approssimazione di poligoni, il codice cerca un contorno con 4 vertici, presumibilmente rappresentante la targa del veicolo.

### Riconoscimento della Targa tramite OCR
Se viene individuato un contorno valido, viene estratta la regione della targa e sottoposta all'OCR di Tesseract per il riconoscimento del testo.

### Visualizzazione delle Immagini
L'immagine originale viene visualizzata con il contorno della targa evidenziato in rosso. Viene anche mostrata la regione ritagliata contenente il testo della targa.

### Chiusura dell'Applicazione
L'applicazione rimane in attesa che l'utente prema un tasto e successivamente chiude tutte le finestre visualizzate.

