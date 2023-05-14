# MIT License
# Copyright (c) 2023 Emir Memic
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# important (used sources for writing this script) and useful (for improving the script):
# developed in python 3.7 and qt5 
# https://note.nkmk.me/en/python-pillow-concat-images/
# https://stackoverflow.com/questions/47483951/how-to-define-a-threshold-value-to-detect-only-green-colour-objects-in-an-image


print ('hello me')

import os, sys, glob
import cv2
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image #, ImageDraw

from greenSearchUserInterface import Ui_MainWindow

print ('works?')

class WindowInt(QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       
        print ('hello me again')
        print ('...')
        
        print ('hello moi')
        
        self.ui.pushButton.clicked.connect(self.show_histagram)
        self.ui.pushButton_2.clicked.connect(self.list_available_images)
        self.ui.pushButton_3.clicked.connect(self.find_green)
			

    def list_available_images(self):

        self.ui.listWidget.clear()

        selectDir = QFileDialog.getExistingDirectory()
        print ('selectDir', selectDir)
        self.ui.lineEdit.setText(selectDir)
        
        listOfImagesAnalysis = []
        #for images in glob.glob1(selectDir, '*.mp4'):
        for images in glob.glob1(selectDir, '*.jpg'):	
            listOfImagesAnalysis.append(images)
        self.ui.listWidget.addItems(listOfImagesAnalysis)	

    def show_histagram(self):

        for selectedMp4 in self.ui.listWidget.selectedItems():
            photoRead = str(selectedMp4.text())

            print (photoRead)

            pathToFile = str(self.ui.lineEdit.text()) + '//'

            target_image = pathToFile + photoRead
            img_0 = cv2.imread(target_image)

            hsv_image = cv2.cvtColor(img_0, cv2.COLOR_BGR2HSV)
            hue = hsv_image[:,:,0]
            sat = hsv_image[:,:,1]
            val = hsv_image[:,:,2]

            mean_hue = np.mean(hue)
            mean_sat = np.mean(sat)
            mean_val = np.mean(val)

            median_hue = np.median(hue)
            median_sat = np.median(sat)
            median_val = np.median(val)

            min_hue = int(np.min(hue))
            min_sat = int(np.min(sat))
            min_val = int(np.min(val))

            max_hue = int(np.max(hue))
            max_sat = int(np.max(sat))
            max_val = int(np.max(val))
             
            print ('hue mean - median:', mean_hue, '-', median_hue)
            print ('hue min - max    :', min_hue,'-', max_hue)
            print ('sat mean - median:', mean_sat, '-', median_sat)
            print ('sat min - max    :', min_sat,'-', max_sat)
            print ('val mean - median:', mean_val, '-', median_val)
            print ('val min - max    :', min_val,'-', max_val)

            plt.figure(figsize=(10,10))
            plt.subplot(311)                             #plot in the first cell
            plt.subplots_adjust(hspace=.5)
            plt.title("Hue")
            plt.hist(np.ndarray.flatten(hue), bins=180)
            plt.subplot(312)                             #plot in the second cell
            plt.title("Saturation")
            plt.hist(np.ndarray.flatten(sat), bins=128)
            plt.subplot(313)                             #plot in the third cell
            plt.title("Luminosity Value")
            plt.hist(np.ndarray.flatten(val), bins=128)
            plt.show()

    def find_green(self):

        try:
            os.mkdir(str(self.ui.lineEdit.text()) + '//' + 'ProcessedOutputFiles')
        except:
            print ('./IntermediateOutputs directory exists!')


        if int(str(self.ui.lineEdit_2.text())) < 0:
            self.ui.lineEdit_2.setText('0')
        if int(str(self.ui.lineEdit_4.text())) < 0:
            self.ui.lineEdit_4.setText('0')
        if int(str(self.ui.lineEdit_6.text())) < 0:
            self.ui.lineEdit_6.setText('0')

        if int(str(self.ui.lineEdit_3.text())) >= 180:
            self.ui.lineEdit_3.setText('179')
        if int(str(self.ui.lineEdit_5.text())) >= 256:
            self.ui.lineEdit_5.setText('255')
        if int(str(self.ui.lineEdit_7.text())) >= 256:
            self.ui.lineEdit_7.setText('255')

        if int(str(self.ui.lineEdit_2.text())) > int(str(self.ui.lineEdit_3.text())):
            self.ui.lineEdit_3.setText(str(self.ui.lineEdit_2.text()))
        if int(str(self.ui.lineEdit_4.text())) > int(str(self.ui.lineEdit_5.text())):    
            self.ui.lineEdit_5.setText(str(self.ui.lineEdit_4.text()))
        if int(str(self.ui.lineEdit_6.text())) > int(str(self.ui.lineEdit_7.text())):
            self.ui.lineEdit_7.setText(str(self.ui.lineEdit_6.text()))

        def get_concat_v(im1, im2):

            # dst = Image.new('RGB', (im1.width, im1.height + im2.height))
            # dst.paste(im2, (0, 0))
            # dst.paste(im1, (0, im2.height))					            
            # return dst	
            dst = Image.new('RGB', (im1.width + im2.width, im1.height))
            dst.paste(im1, (0, 0))
            dst.paste(im2, (im1.width, 0))
            return dst



        for selectedMp4 in self.ui.listWidget.selectedItems():
            photoRead = str(selectedMp4.text())

            pathToFile = str(self.ui.lineEdit.text()) + '//'

            target_image = pathToFile + photoRead

            print (photoRead)

            #target_image = photoRead
            img_0 = cv2.imread(target_image)

            hsv_image = cv2.cvtColor(img_0, cv2.COLOR_BGR2HSV)

            h_min = int(str(self.ui.lineEdit_2.text()))
            h_upper = int(str(self.ui.lineEdit_3.text()))	
            
            s_min = int(str(self.ui.lineEdit_4.text()))
            s_upper = int(str(self.ui.lineEdit_5.text()))

            v_min = int(str(self.ui.lineEdit_6.text()))	
            v_upper = int(str(self.ui.lineEdit_7.text()))
                    

            mask = cv2.inRange(hsv_image, (h_min, s_min, v_min), (h_upper, s_upper, v_upper))

            whole_image = mask.size
            # imask = mask>0
            # green = np.zeros_like(img_0, np.uint8)
            # green[imask] = img_0[imask]
            # green_activ = green[imask].size

            green_activ = np.count_nonzero(mask)
            
            print ('whole_image', whole_image, '\n', 'green_activ', green_activ)

            percent_cover = (float(green_activ) / float(whole_image))*100
            print ('green pixels percentage\t\t\t:', percent_cover, '%')


            self.ui.textBrowser.append(str(photoRead) + '\t' + 'Green pixels (%): ' + str(round(percent_cover, 2)))           

            #cv2.imwrite('Filtered.jpg' , mask)
            color_img = cv2.bitwise_and(img_0,img_0, mask= mask)
            cv2.imwrite(str(pathToFile + '//' +  photoRead.split('.')[-2]) + '_Filtered.jpg', color_img)    

            img1 = cv2.imread(str(pathToFile + '//' +  photoRead.split('.')[-2]) + '.jpg')
            cv2.imwrite(str(pathToFile + '//' +  photoRead.split('.')[-2]) + '_s.jpg', img1)
            img2= cv2.imread(str(pathToFile + '//' +  photoRead.split('.')[-2]) + '_Filtered.jpg')
            cv2.imwrite(str(pathToFile + '//' +  photoRead.split('.')[-2]) + '_s_Filtered.jpg', img2)

            im1 = Image.open(str(pathToFile + '//' +  photoRead.split('.')[-2]) + '_s.jpg')
            im2 = Image.open(str(pathToFile + '//' +  photoRead.split('.')[-2]) + '_s_Filtered.jpg')
            

            
            get_concat_v(im1, im2).save(pathToFile + '//' + 'ProcessedOutputFiles' + '//' +  photoRead.split('.')[-2] + '_OriginalAndFiltered.jpg')


            # color_img = cv2.bitwise_and(img_0,img_0, mask= mask)
            # cv2.imwrite(str(pathToFile + '//' +  photoRead.split('.')[-2]) + '_FilteredColor.jpg', color_img)

        self.ui.textBrowser.append('\n')   
        
    def closeEvent(self, event):

        print ('EXIT all running threads...')
        sys.exit(app.exec_())
        #app.exit()        
        
        
if __name__ == '__main__':
    
    #app = QtWidgets.QApplication(sys.argv)
    #for qt5
    app = QApplication(sys.argv)
    Interface = WindowInt()
    Interface.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint)	
    Interface.show()
    sys.exit(app.exec_())			        