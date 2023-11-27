from clases import *
def main ():
    sis = Sistema()
    while True:
        print('_____MENÚ_____')
        menu = int(input('Elija una opción: \n1.Manipulacón de imágenes \n2.Manipulacion de DICOM \n3.Salir: '))
        
        if menu == 1:
            op = int(input('Ingrese una opcion: \n1.Ingresar una imagen \n2.Hacer recorte de imagen \n3.Volver al menu anterior: '))

            if op == 1:
                print('A continuación se muetran los nombres de las imágenes disponibles:')
                nombres = os.listdir('imagenes')#imagenes cargada previamente
                c=0
                for i in nombres:
                    c += 1
                    a = str(c)
                    print(a+'. '+ i)
                selc = input('Ingrese nombre de la imagen que desea guardar: ')
                img = Celula()
                img.cargaArchivo(selc)
                img.verHistograma()
                #plt.imshow(img.matriz())
                #plt.show()
                sis.guardarImg(img, selc)

            elif op == 2:
                print('A continuación se muestran las imagenes cargadas en el sistema: ')
                for i in sis.verLlavesImg():
                    print(i)
                name = input('Ingrese el nombre de la imagen a escalonar y a recortar: ')
                img = sis.verImg(name)
                x= float(input('Ingrese el numero que dessée escalonar: '))
                x1= int(input('Ingrese la cordenada inicial en  x: '))
                x2= int(input('Ingrese el ancho del area a recortar: '))
                y1= int(input('Ingrese la coordenada inicial en y: '))
                y2= int(input('Ingrese la altura del area a recortar: '))
                plt.imshow(img.matriz())
                editada = img.escalado(x,x1,x2,y1,y2)
                
                plt.imshow(img.matriz())
                #cv2.imshow('Imagen alterada',editada)
                plt.show()
            elif op== 3:
                continue

            else:
                print('Opcion no valida')
        
        elif menu == 2:
                menu2 =int(input('Ingrese una opción: \n1.Cargar repositorio de archivo DCM \n2.Guardar un archivo DCM \n3.Anonimizar datos \n4.Extraer imagen y ecualizar \n5.Volver al menu anterior: '))
                if menu2== 1:
                    op = int(input('Elija: \n1. Usar repositorio por defecto \n2.Ingrese repositorio \n3.Volver al menu anterior:'))
                    if op == 1:
                        ruta = 'MPRAGE_GRAPPA'
                        arch = DICOM()
                        arch.showNombres()

                        n = input('Ingrese el nombre con el que desse guardar el repositorio: ')
                        sis.guardarDicom(n,arch)
                        if sis.guardarDicom(n,arch) == True:
                            print('Se ha ingresado correctamente')

                    elif op == 2:
                        pass

                    elif op== 3:
                        continue
                    else:
                        print('Opción no valida')

                elif menu2 == 2:
                    print('A continuación se muestra los repositorios disponibles: ')

                    for i in sis.verLlavesDicom():
                        print(i)
                    name=input('Ingrese nombre del repositorio que desea: ')
                    archivo = sis.verDICOM(name)
                    print('A continuación el nombre de los archivos disponibles: ')
                    archivo.showNombres()
                    ndcm = input('Ingrese el nombre del archivo: ')
                    ruta =  f'{archivo.verRuta()}\{ndcm}'
                    dcm = archivo.leer_dataset(ruta)
                    a= archivo.guardarDcm(dcm,ndcm)
                    if a==True:
                        print('El archivo se ha leido con exito')

                elif menu2 == 3:
                    print('A continuación se muestra los repositorios disponibles: ')

                    for i in sis.verLlavesDicom():
                        print(i)
                    name=input('Ingrese nombre del repositorio que desea: ')
                    archivo = sis.verDICOM(name)
                    print('A continuacion se muestran los archivos.dcm guardados: ')
                    for i in archivo.verDcms():
                        print (i)

                    n = input('Ingrese el nombre del archivo que  desea anonimizar: ')
                    dcm = archivo.ver_unArchivo(n)
                    archivo.metadata(n)
                    #ANONIMIZAR
                    dcm.PatientName ='N/A' 
                    dcm.PatientID = 'N/A' 
                    dcm.PatientBirthDate ='N/A' 
                    dcm.PatientSex ='N/A' 
                    dcm.PatientAge ='N/A' 
                    dcm.PatientWeight = 0
                    newnombre = input('Ingrese nuevo nombre para el archivo anonimizado: ') 
                    dcm.save_as(f'New_DICOM\{newnombre}.dcm')
                    print('Datos anonimizados guardados en: la carpeta New_DICOM')
                
                elif menu2 == 4:
                    print('A continuación se muestra los repositorios disponibles: ')

                    for i in sis.verLlavesDicom():
                        print(i)
                    name=input('Ingrese nombre del repositorio que desea: ')
                    archivo = sis.verDICOM(name)
                    print('A continuacion se muestran los archivos.dcm guardados: ')
                    for i in archivo.verDcms():
                        print (i)

                    n = input('Ingrese el nombre del archivo que  desea anonimizar: ')
                    #dcm = archivo.ver_unArchivo(n)
                    imagen = archivo.pixel_array(n)
                    imagen_eq = cv2.equalizeHist(imagen)
                    plt.figure(figsize=(10, 5))
                    plt.subplot(1, 2, 1)
                    plt.imshow(imagen, cmap='gray')
                    plt.title('Imagen Original')

                    plt.subplot(1, 2, 2)
                    plt.imshow(imagen_eq, cmap='gray')
                    plt.title('Imagen Ecualizada')

                    plt.show()

                elif menu2 == 5:
                    continue
                else:
                    print('Opcion no valida')

        elif menu == 3:
            break
        else:
            print('Opción no valida')
            print("hola ")


                    



main()

#PPMI_3832_MR_MPRAGE_GRAPPA__br_raw_20140131101904737_22_S211651_I412208.dcm
    