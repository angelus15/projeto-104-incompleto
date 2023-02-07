import cv2

img = cv2.imread("solar-system.jpg")
cv2.imshow("mostrar imagem",img)

cv2.putText(img,
             "Sol",
             (100,70),
             cv2.FONT_HERSHEY_COMPLEX,
             2,  
             (0,0,255)               
             )

cv2.putText(img,
             "Mercurio",
             (100,60),
             cv2.FONT_HERSHEY_COMPLEX,
             2,  
             (0,0,255)               
             )

cv2.putText(img,
             "Venus",
             (100,50),
             cv2.FONT_HERSHEY_COMPLEX,
             2,  
             (0,0,255)               
             )

cv2.putText(img,
             "Terra",
             (100,40),
             cv2.FONT_HERSHEY_COMPLEX,
             2,  
             (0,0,255)               
             )

cv2.putText(img,
             "Marte",
             (100,30),
             cv2.FONT_HERSHEY_COMPLEX,
             2,  
             (0,0,255)               
             )

cv2.putText(img,
             "jupter",
             (100,20),
             cv2.FONT_HERSHEY_COMPLEX,
             2,  
             (0,0,255)               
             )

cv2.putText(img,
             "Saturno",
             (100,10),
             cv2.FONT_HERSHEY_COMPLEX,
             2,  
             (0,0,255)               
             )

cv2.putText(img,
             "Urano",
             (100,0),
             cv2.FONT_HERSHEY_COMPLEX,
             2,  
             (0,0,255)               
             )

cv2.putText(img,
             "Plutao",
             (100,-10),
             cv2.FONT_HERSHEY_COMPLEX,
             2,  
             (0,0,255)               
             )

cv2.waitKey(0)