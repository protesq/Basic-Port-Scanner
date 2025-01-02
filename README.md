
# Port Tarayıcı

Bu, hedef IP adresinin ilk 1024 portunu taramak için tasarlanmış basit bir Python tabanlı port tarayıcıdır. 
Script, daha hızlı tarama için çoklu iş parçacığı (threading) kullanır ve belirtilen hedefte açık portları raporlar.

## Özellikler
- 1'den 1024'e kadar olan portları tarar.
- Açık portları görüntüler.
- Verimli tarama için çoklu iş parçacığı kullanır.
- Kullanıcıya tarama süresini sağlar.

## Gereksinimler
- Python 3.x
- Socket ve threading modülleri (Python ile dahili olarak gelir).

## Kullanım
1. Script'i çalıştırın:
    ```
    python portscanner.py
    ```
3. İstenildiğinde hedef IP adresini girin.

## Örnek
```
==================================================
Port Tarayıcı
==================================================
Hedef IP adresini girin: 192.168.1.1

Tarama başlıyor: 192.168.1.1
Port 22 açık
Port 80 açık

Tarama tamamlandı! Süre: 0:00:10.123456
```

## Notlar
- Bu script yalnızca eğitim ve yetkilendirilmiş kullanım için tasarlanmıştır.
- Herhangi bir IP adresini taramadan önce izin aldığınızdan emin olun.

## Sorumluluk Reddi
Bu aracın yanlış kullanımından yazar sorumlu tutulamaz.
