# GitHub Repo Bilgilerini CSV Formatında İndirme

Bu proje, belirli bir GitHub kullanıcısının tüm repo bilgilerini alarak CSV dosyasına kaydeden basit bir Python betiğidir. Repo bilgileri, API üzerinden alınır ve CSV formatında bir dosyaya yazılır. Böylece, GitHub üzerindeki tüm reposuna ait bilgilere kolayca erişebilirsin.

## Gereksinimler

Bu betiği çalıştırmak için aşağıdaki yazılımlara ihtiyacın var:

- Python 3.x
- requests kütüphanesi (API'den veri çekmek için)
  
`requests` kütüphanesini yüklemek için terminal ya da komut satırında aşağıdaki komutu çalıştırabilirsin:

```bash
pip install requests
```

## Kullanım

1. Proje dosyalarını indir veya kopyala.
2. `script.py` dosyasının içerisindeki `username` değişkenine kendi GitHub kullanıcı adını yaz.
3. Python betiğini çalıştır:

```bash
python script.py
```

4. Script çalıştıktan sonra, proje klasöründe `github_repos.csv` adında bir dosya oluşacak. Bu dosyada, kullanıcıya ait repo bilgileri bulunur.

## Çıktı Dosyası

- CSV dosyasındaki kolonlar:
  - Repo Adı: Projenin adı
  - Açıklama: Proje açıklaması
  - Dil: Projenin yazıldığı dil
  - Yıldız Sayısı: GitHub'daki yıldız sayısı
  - Fork Sayısı: Repo'nun fork sayısı
  - URL: GitHub repo URL'si

## Lisans

Bu proje GNU lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına göz atabilirsiniz.