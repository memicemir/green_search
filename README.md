# green_search
HUE indicator - color (apearence) based image analysis.
-------------------
Simple python script for sharing and teaching conceptual framework of crop cover analysis in the field based on images (percent of "green" pixels in image - in relative terms).
------------------------
Written in python (v: 3.7) with interface created in qt-designer (qt5).
------------------
Need to be install before:
- python (3.7)
- open cv2
- numpy
- matplotlib
- PIL

If interface is moddified in qt-designer it has to be compiled: "pyuic5 -x greenSearchUserInterface.ui -o greenSearchUserInterface.py".
This py compilation is imported in "greenSearch_v1.py" through "from greenSearchUserInterface import Ui_MainWindow" line in python script.