# License Plate Recognition with OpenCV and Tesseract
Python script that recognizes a license plate from an image, cuts it out and extracts the text using a tesseract

## Demo screenshot
<img width="612" alt="tesseract" src="https://github.com/davpirelli/License-Plate-Recognition-with-OpenCV-Tesseract/assets/6840116/0573fe6d-6383-4d35-a080-527f97eb8ab2">


### Import of bookstores
The Code Begins by The Bookstores Requirector For the Recognition of the Vehicle License Plate, Including OPENCV for the Processing of Images, IMUTILS TO Simplify Some Operations, Numpy for the Manipulation of Array and PytessiRact for the OCR.

### Loading and Prepioxification of the image
The vehicle image is read from files and reduced to 800x600 pixels.Subsequently, a bilateral filter is converted into gray scale to reduce the noise while maintaining the edges.

### Search of contours
Using the Canny edges detection algorithm, the outlines are identified in the pre -empire image.The 10 larger outlines are extracted and ordered by area.

### Identification of the Targa outline
Through the approximation of polygons, the code is looking for an outline with 4 leaders, presumably representing the vehicle plaque.

### recognition of the plaque via OCR
If a valid outline is identified, the plaque region is extracted and subjected to the Tesserace OCR for the recognition of the text.

### Image viewing
The original image is displayed with the side dish of the plaque highlighted in red.The cut region containing the Targa text is also shown.

### Closing of the application
The application is waiting for the user to prema a button and then closes all the windows displayed.
