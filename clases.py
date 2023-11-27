import cv2
import pydicom
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import os
a = cv2.imread('Imagenes\cell.jpg')
plt.imshow(a)
#plt.show()
#print(a)


class Celula ():
    def __init__(self):
        self._archivo = ''#guarda la matriz de imagen
        self._histograma = ''


    def cargaArchivo (self,x):
        self._archivo = cv2.imread('Imagenes'+f'\{x}')
        self._histograma = cv2.calcHist([self._archivo], [0], None, [256], [0, 256])
        return True
    
    def matriz(self):
        return self._archivo
    
    def verHistograma(self):
         plt.plot(self._histograma, color = 'gray')
         plt.show ()

    def escalado(self, escalar, x1,y1,x2,y2):
         
         #Escalado
        factor_escalado = escalar
        nuevo_ancho = int(self._archivo.shape[1] * factor_escalado)#multiplica las culmans por el escalar
        nuevo_alto = int(self._archivo.shape[0] * factor_escalado)#filas
        imagen_escalada = cv2.resize(self._archivo, (nuevo_ancho, nuevo_alto))#recorta la img 

         #recorte
        recorte = imagen_escalada[y1:y1+y2, x1:x1+x2]
        #print(recorte)
        plt.imshow(recorte)
        plt.show()
        return recorte
    
class DICOM():
    def __init__(self, ruta = 'MPRAGE_GRAPPA'):
        self.__carpeta = ruta
        self.__lista_dcm = {}
    

    def verDcms(self):
        return self.__lista_dcm.keys()
    #Dentro de la clase DICOM
    def pixel_array(self, llave):
        img= self.__lista_dcm[llave].pixel_array.astype(np.uint8)
        return img
    
    
    def leer_dataset(self, ruta):
        lec = pydicom.dcmread(ruta)
        return lec
    
    def verRuta(self):
        return self.__carpeta
    
    def guardarDcm(self,dcm,llave):
        self.__lista_dcm[llave] = dcm
        return True
        
    def ver_unArchivo(self, llave):
        return self.__lista_dcm[llave]

    def showNombres(self):
        nombres = os.listdir(self.__carpeta)
        c=0
        for i in nombres:
            c += 1
            a = str(c)
            print(a+'. '+ i)
    
    def metadata(self, llave):

        dcm = self.ver_unArchivo(llave)
        print(f'nombre del paciente: {dcm.PatientName}')
        print(f'Cedula del paciente: {dcm.PatientID}')
        print('Fecha de nacimiento del paciente: N/A')
        print(f'sexo del paciente: {dcm.PatientSex}')
        print(f'Edad del paciente: {dcm.PatientAge}')
        print(f'Peso del paciente: {dcm.PatientWeight}')

class Sistema():
    def __init__(self):
        self.__DICOM = {}
        self.__img = {}

    def guardarDicom(self, name, dicom):
        self.__DICOM[name] = dicom
        return True

    def guardarImg(self, img, name):
        self.__img[name] = img 
        return True
    
    def verImg(self, name):
        if name in self.__img:
            return self.__img[name]
        
    def verLlavesDicom(self):
        return self.__DICOM.keys()
        
    def verLlavesImg(self):
        return self.__img.keys()
    
    def verDICOM(self, name):
        return self.__DICOM[name]

#hola



