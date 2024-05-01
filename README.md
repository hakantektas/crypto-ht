
# Binance USDT Paritelerindeki RSI Değeri Kontrolü Projesi

Bu proje, Binance kripto borsasında yer alan USDT paritelerindeki coinlerin RSI (Relative Strength Index) değerlerini kontrol eden bir Python betiği içerir. 

*** Binance kripto borsasında USDT paritesinde işlem gören coinlerin RSI değerlerini kontrol etmek için oluşturulmuştur. 

*** RSI değeri 29'un altında olan coinlerin listesini oluşturur.
 

## Kullanım/Örnekler/Gereksinimler


**1. Python Kurulumu:** Bu betik Python 3 ile yazılmıştır. Bilgisayarınızda Python 3'ün yüklü olduğundan emin olun.

**2. Gerekli Modüllerin Yüklenmesi:** Betiği çalıştırmadan önce, gerekli Python modüllerini yüklemeniz gerekebilir. Gerekli modüllerin yüklenmesi için terminal veya komut istemcisinde şu komutu kullanabilirsiniz:

`requests`: HTTP istekleri yapmak için kullanılır.

```javascript
pip install requests
```

**3. Betiği Çalıştırma:** Betiği çalıştırmak için terminal veya komut istemcisini açın ve betiğin bulunduğu dizine gidin. Daha sonra aşağıdaki komutu kullanarak betiği çalıştırın:


Betik, RSI değeri 29'un altında olan coinlerin sembollerini json dosyasına yazdırır ,

```javascript
python getSymbol.py
```

RSI değeri 29'un altında olan coinleri ve RSI değerlerini console da yazdırır.

```javascript
python crypto_rsi.py
```

**4. Sonuçları Görüntüleme:** Betik, RSI değeri 29'un altında olan coinlerin sembollerini ve RSI değerlerini ekrana yazdırır.

  
## Özellikler

- RSI (Relative Strength Index), bir varlığın fiyat değişim hızını ve büyüklüğünü analiz etmek için kullanılan bir teknik göstergedir. 
- Bu Python betiği, her bir USDT paritesi için RSI değerini hesaplar ve RSI değeri 29'un altında olanları ekrana yazdırır.
- Bunu gerçekleştirmek için Binance API'sini kullanır ve her bir coin için son 14 saatlik kapanış fiyatlarını alır.
- Son olarak, RSI değerini hesaplar ve eğer 29'un altındaysa, coinin sembolünü ve RSI değerini ekrana yazdırır.
- Bu betiği çalıştırarak, Binance kripto borsasındaki USDT paritesindeki coinlerin RSI değeri 29'un altında olanlarını listeleyebilirsiniz.
 
## Ortam Değişkenleri

Bu projeyi çalıştırmak için aşağıdaki ortam değişkenlerini .env dosyanıza eklemeniz gerekecek

`API_KEY`

`ANOTHER_API_KEY`

  
## Yükleme 

crypto-ht'i npm kullanarak yükleyin

```bash 
  npm i cripto-ht
  cd your_path/cripto-ht
```
    
## Çalıştırın

RSI değeri 29 ve altında olan USDT paritesine sahip kripto paraları listelemek için çalıştırın

```bash
  npm run getRSI
```

  
## Bilgisayarınızda Çalıştırın

Projeyi klonlayın

```bash
  git clone https://link-to-project
```

Proje dizinine gidin

```bash
  cd crypto-ht
```

Gerekli paketleri yükleyin

```bash
  npm i cripto-ht
```

RSI değeri 29 ve altında olan USDT paritesine sahip kripto paraları listelemek için çalıştırın

```bash
  npm run getRSI
```

Binance borsasından tüm USDT paritelerini çeken ve bu pariteleri JSON formatında bir dosyaya yazdırmak için çalıştırın

```bash
  npm run getSymbol
```
  
## Kullanılan Teknolojiler

Bu betik Python 3 ile yazılmıştır ve  https://openai.com/ tarafından sağlanan GPT-3 tabanlı bir yardımcı ile oluşturulmuştur.

Bilgisayarınızda Python 3'ün yüklü olduğundan emin olun.Aşağıdaki adımları takip ederek yükleyebilirsiniz .

Binance API'leri kullanılmıştır . Daha fazlası için Binance API'leri incelenebilir . https://binance-docs.github.io/apidocs/spot/en/#introduction 


**Windows**

**1. Python.org'dan İndirme:**
Python'un resmi web sitesi olan Python.org'dan Windows için Python 3 sürümünü indirin. İndirme sayfasına buradan ulaşabilirsiniz.

**2. Kurulum:**
İndirdiğiniz dosyayı çalıştırarak Python 3'ü kurun. Kurulum sırasında, "Add Python 3.x to PATH" seçeneğini işaretleyerek Python'un PATH değişkenine otomatik olarak eklenmesini sağlayabilirsiniz.

**3. Kontrol:**
Python'un doğru şekilde yüklendiğinden emin olmak için bir komut istemi (Command Prompt) açın ve aşağıdaki komutu girin:

```
python --version
```


**macOS**

**1. Homebrew ile Kurulum:**

Eğer Homebrew yüklü değilse, önce Homebrew'ü kurun:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Ardından, aşağıdaki komutu kullanarak Python 3'ü yükleyin:

```
brew install python
```
**2. Kontrol:**
Python'un doğru şekilde yüklendiğinden emin olmak için bir terminal açın ve aşağıdaki komutu girin:

```
python3 --version
```
Bu komut Python'un yüklü olduğu sürüm numarasını yazdıracaktır.

**Linux (Ubuntu/Debian)**

**1. Apt ile Kurulum:**
Terminal açın ve aşağıdaki komutu kullanarak Python 3'ü yükleyin:
```
sudo apt update
sudo apt install python3
```
**2. Kontrol:**
Python'un doğru şekilde yüklendiğinden emin olmak için bir terminal açın ve aşağıdaki komutu girin:
```
python3 --version
```
Bu komut Python'un yüklü olduğu sürüm numarasını yazdıracaktır.
Bu adımları izleyerek, işletim sisteminize Python 3'ü kolayca yükleyebilirsiniz.
  


**Katkıda Bulunma**

Bu projeye katkıda bulunmak isterseniz, lütfen bir GitHub issue açın veya bir pull request gönderin.

## Ekran Görüntüleri

![Uygulama Ekran Görüntüsü](<img width="572" alt="Screenshot 2024-05-01 at 23 01 24" src="https://github.com/hakantektas/crypto-ht/assets/72494835/f2dd8cf4-72a1-4ba9-a2f6-b8aaf23c1bf2">)

  