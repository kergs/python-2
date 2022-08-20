import pywhatkit as kit
import cv2

print("Enter your Text to convert in Handwriting")
Handwritten = input(":>>")
kit.text_to_handwriting(Handwritten, save_to="pythoncoding.png")
img = cv2.imread("pythoncoding.png")
cv2.imshow("Python Coding", img)
cv2.waitkit(0)
cv2.destroyAllWindow()
