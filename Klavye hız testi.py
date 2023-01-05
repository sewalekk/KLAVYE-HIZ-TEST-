# Klavye hız testi

import time
import datetime

print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
time.sleep(0.5)

zaman=datetime.datetime.now()

print("Elektronik bir donanımı, belirli bir işi yapması için derlenmiş komutların bütününe yazılım denir. En sade bir halde böyle yorumlanır ama uygulamaya gelince bu kadar sade değildir. Yazılım hayatımızın her yerindedir.Yazılım aslında hayatımızın her alanındadır. Bu haliyle yazılım aslında hayatımızı kolaylaştırır. Bilgisayarlar, telefonlar, televizyonlar, mobil teknoloji, internet, sanayide kullanılan yeni nesil cihazların neredeyse tamamı, otomotiv, inşaat, eğitim, reklam, pazarlama, iletişim, medya, eğlence, sağlık başta olmak üzere hemen hemen tüm sektörlerde, uzay sanayisinde, günlük hayatta kullanılan bazı teknik aksesuarlarda kısacası “yazılım” gerçekten de yaşamın her alanındadır.")

metin=input("Yazmaya Başlayınız: ")
zaman2=datetime.datetime.now()

yazim_hizi=zaman2-zaman
saniye=round(yazim_hizi.total_seconds(),2)
zaman3=round(len(metin)/saniye,1)

print("Toplam Süre: {}".format(saniye))
print("{} kelime başına".format(zaman3))

