import socket
import threading
from datetime import datetime

def port_tara(hedef, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 saniyelik timeout
        sonuc = sock.connect_ex((hedef, port))
        if sonuc == 0:
            print(f"Port {port} açık")
        sock.close()
    except:
        pass

def main():
    # Banner
    print("=" * 50)
    print("Port Tarayıcı")
    print("=" * 50)
    
    # Hedef IP'yi al
    hedef = input("Hedef IP adresini girin: ")
    try:
        hedef_ip = socket.gethostbyname(hedef)
    except socket.gaierror:
        print("Hata: Geçersiz host adı")
        return
    
    # Tarama başlangıç zamanı
    print(f"\nTarama başlıyor: {hedef_ip}")
    baslangic = datetime.now()
    
    # Port tarama
    try:
        for port in range(1, 1025):  # İlk 1024 portu tara
            thread = threading.Thread(target=port_tara, args=(hedef_ip, port))
            thread.start()
            
        # Ana thread'in tüm alt thread'lerin bitmesini beklemesi
        main_thread = threading.current_thread()
        for thread in threading.enumerate():
            if thread is not main_thread:
                thread.join()
                
    except KeyboardInterrupt:
        print("\nTarama iptal edildi!")
        return
    except socket.error:
        print("\nBağlantı kurulamadı!")
        return
        
    # Tarama bitiş zamanı
    bitis = datetime.now()
    toplam = bitis - baslangic
    print(f"\nTarama tamamlandı! Süre: {toplam}")

if __name__ == "__main__":
    main()