import requests, os, time, png, pyqrcode
from colorama import Fore, Back, Style

bersih = lambda:os.system('clear')

def banner():
    bersih()
    print(Fore.CYAN+"""
  ____    ___           __  
 / __ \  / _ \_______  / /__
/ /_/ / / , _/ __/ _ \/  '_/
\___\_\/_/|_|\__/\___/_/\_\ 
                            
"""+Style.RESET_ALL)
    print("""

        {}[1] Generate QRCode

        {}[0] Keluar Tools

          """.format(Fore.GREEN, Style.RESET_ALL))


def main():
    banner()
    try:
        c = True
        while c:
            cek = str(input("Masukan No Menu : "))
            if (cek == "1"):
                banner()
                link = str(input("Masukan URL : "))
                output_name = str(input("Masukan Nama Output : ex (nama_output.png): "))
                print(Fore.YELLOW+"Proses.....")
                time.sleep(5)
                bersih()
                qr_code = pyqrcode.create(link)
                qr_code.png(f'{output_name}', scale=5)
                print(Fore.GREEN+"Generate Berhasil....")
                print(Fore.YELLOW+"Output QrCode Tersimpan : {}".format(output_name))
                time.sleep(3)
                back = str(input("Generate QRCode Lagi? [y/n]: "))
                if "y" in back:
                    main()
                else:
                    exit()
            elif (cek == "0"):
                c = False
            else:
                print("Menu Nggak Ada!")
                c = False

    except Exception as e:
        print(e)



if __name__ == '__main__':
    main()
