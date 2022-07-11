from ftplib import FTP
import os

ftp = FTP()

def download(host, user, password, remoteRute,file, *localRute):
    
    # Nos conectamos y decimos que FTP(valores) = ftp
    with FTP(host, user, password, encoding="utf-8", timeout=3.0) as ftp:

        # Nos desplazamos al directorio.
        ftp.cwd(remoteRute)
        print(ftp.pwd())
        
        # Comprobamos si se quiere desplazar a alguna ruta local.
        if localRute == True:
            os.chdir(localRute)
        else:
            pass
        
        # Descargamos el archivo
        with open(file, "wb") as f:
                            def callback(data):
                                f.write(data)
                                
                            ftp.retrbinary('RETR %s' % file, callback)


        # Cerramos conexión
        ftp.close()
        

def upload(host, user, password, remoteRute, file, *localRute):
    
    # Nos conectamos y decimos que FTP(valores) = ftp
    with FTP(host, user, password, encoding="utf-8", timeout=3) as ftp:

        # Nos desplazamos al directorio.
        ftp.cwd(remoteRute)
        print(ftp.pwd())
        
        # Comprobamos si se quiere desplazar a una ruta local.
        if localRute == True:
            os.chdir(localRute)
        
        # Abrimos el achivo (en lectura)
        f = open(file, 'rb')
        
        # Subimos el archivo.
        ftp.storbinary(f'STOR {file}', f)

        # Cerramos conexión
        ftp.close()
        
        
def delFile(host, user, password, remoteRute, file):
    
    with FTP(host, user, password) as ftp:
        
        # Nos movemos a la ruta remota.
        ftp.cwd(remoteRute)
        # Eliminamos el archivo.
        ftp.delete(file)
        
        # Cerramos conexión
        ftp.close()
            

def delDirectory(host, user, password, remoteRute, directory):
    
    with FTP(host, user, password) as ftp:
        
        # Nos movemos a la ruta remota.
        ftp.cwd(remoteRute)
        # Eliminamos el directorio
        ftp.rmd(directory)
        
        # Cerramos la conexión.
        ftp.close()

def moverse(host, user, password):
    
    with FTP(host, user, password, encoding="utf-8", timeout=3) as ftp:
        while True:
            
            print(ftp.pwd())
            print(ftp.dir())
            
            option = input("Take the option:\n[1]\tMoverse a directorio.\n[2]\tSalir\n")
            
            if option == "1":
                directory = input("How directory?\n")
                ftp.cwd(directory)
                print(ftp.pwd())
                print("aqui llega")
                """ directory = input("How directory?\n") """
                
            if option == "2":
                print("Bye")
                break
                
        ftp.close()
        
