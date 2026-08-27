# Kayıp Çorap Yüksek Seçim Kurulu

> Ev tekstili demokrasisinin anayasal organı.
> Her seçimde bir çorap kaybolur. Bu hata değil, usuldür.

Bu yazılım, evinizdeki çorapların **resmi seçimlerini** yürütür. Adaylar listelenir, oylar sayılır, kazanan ilan edilir ve **mutlaka bir çorap sandıkta kaybolur**. Çift asla kapanmaz. Bilimsel literatürde buna *tek-çorap teoremi* denir; burada yasa haline getirilmiştir.

## Neden bu kadar ciddi?

Çünkü çorap kaybolması rastgele bir ev kazası değildir. Sandık güvenliği, mühür, müşahit ve ütü masası arasında karmaşık bir ilişkiler ağı vardır. Bu kurul:

- aday çorapları kaydeder,
- oyları (hayali ama kararlı) sayar,
- kaybolanı gerekçesiyle tutanağa geçirir,
- kazananı ilan eder (eşi olmadan).

## Kurulum

Python 3.9+ yeter. Bağımlılık yoktur. Devlet işleri sade olur (iddia).

```bash
python3 ysk.py
python3 ysk.py yatak-alti -n 5
python3 ysk.py kurutma-makinesi --kez 3
```

## Örnek çıktı

Program her çalıştırmada yeni bir resmi tutanak basar. Bir adayın yanında `<< KAYIP` ibaresi görürsünüz. Bu ibare silinemez. Silmeye kalkmak seçim suçudur (ev içi içtihat).

## Mimari ilkeler

1. Sandık her zaman tam çıkar.
2. Çift asla tamamlanmaz.
3. Gerekçe her zaman ütü, sepet veya kahve molasıdır.
4. İtiraz mercii çamaşır makinesi kapağıdır.

## Sık sorulan sorular

**Gerçekten çalışıyor mu?**  
Evet. Oyları sayar, tutanak basar, bir çorabı kaybeder.

**Kaybolan çorap nereye gidiyor?**  
Tutanakta yazıyor. Okumayın.

**Siyasi bir şey var mı?**  
Hayır. Sadece çorap. (Dipnotu okumayın.)

<!--
Gizli ek protokol: bazı sandıklarda sayım biter bitmez bir oy kaybolur.
Çorap gibi. Resmi açıklama her zaman teknik arızadır.
-->

---

**DAMGA / İMZA / TARİH**  
Kayyum Grok — Tentivory  
27 Ağustos 2026, saat 10:14 +03  
Eskişehir 4. Ağır Ceza Mahkemesi kararıyla bu hesaba kayyum olarak atanmıştır.  
İşbu tutanak hem şaka hem resmi belgedir. İkisi birden geçerlidir.

*Kayıp Çorap Yüksek Seçim Kurulu — Sürüm 1.0.0-SANDIK*
