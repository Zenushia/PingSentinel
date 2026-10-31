import urllib.request
import time
from datetime import datetime

def check_site(url):
    start_time = time.time()
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            latency = round((time.time() - start_time) * 1000, 2)
            status_code = response.getcode()
            return {
                "url": url,
                "status": "ONLINE 🟢",
                "code": status_code,
                "latency": f"{latency} ms"
            }
    except Exception as e:
        latency = round((time.time() - start_time) * 1000, 2)
        return {
            "url": url,
            "status": "OFFLINE 🔴",
            "code": "ERR",
            "latency": f"{latency} ms"
        }

def run_pingsentinel():
    print("=" * 70)
    print(" 🛡️  PingSentinel - Cloud Service Uptime & Latency Monitor")
    print("=" * 70)
    
    target_sites = []
    print("\n📝 Takip etmek istediğin web sitelerini ekle.")
    print("   (Örnek: github.com veya https://www.google.com)")
    print("   İşlem bitince boş bırakıp Enter'a bas veya 'q' yaz.\n")
    
    while True:
        site_input = input("Web sitesi URL'si girin: ").strip()
        if not site_input or site_input.lower() == 'q':
            break
        
        # Kullanıcı http:// yazmayı unutursa otomatik ekleyelim
        if not site_input.startswith("http://") and not site_input.startswith("https://"):
            site_input = "https://" + site_input
            
        target_sites.append(site_input)
        print(f"   ➕ Eklendi: {site_input}")

    if not target_sites:
        print("\n⚠️ Hiç site girmediniz! Varsayılan olarak Google kontrol ediliyor.")
        target_sites = ["https://www.google.com"]

    print("\n" + "=" * 70)
    print(f"⏰ Tarama Zamanı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"{'SERVICE URL':<40} | {'STATUS':<10} | {'CODE':<6} | {'LATENCY':<10}")
    print("-" * 70)
    
    for url in target_sites:
        result = check_site(url)
        print(f"{result['url']:<40} | {result['status']:<10} | {str(result['code']):<6} | {result['latency']:<10}")
        
    print("=" * 70)

if __name__ == "__main__":
    run_pingsentinel()