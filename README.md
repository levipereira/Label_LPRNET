# Label LPRNET
Nvidia LPRNet (License Plate Recognition Net) 
Label_LPRNET  is a graphical image annotation tool for build/validate Dataset on LPRNET Format.
Each cropped license plate image has a corresponding label text file that contains one line of characters in the specific license plate. 



## Requirement
- ### python 3
- ### pyQt5
- ### opencv-python


##  New Features on this Fork
- #### Save Last Session. i.e When reopen dir it continues from the last image that was processed.
- #### Added Delete Function
- #### Added Shortcuts 
    NEXT : KEY UP
    BACK : KEY DOWN
    DELETE : PAGE DOWN
- #### Changed Layout


![logo](label_lprnet01.jpg)

##  Instructions:
When Browser a DIR please choose Root_DIR  eg. train_01 
The train_01 must contain image and label dirs
image dir : All images
label dir : All txt files
The Label LPRNET will read all images from image dir and all labels from label dir
![logo](label_lprnet02.jpg)

