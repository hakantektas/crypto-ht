const { exec } = require('child_process');

function runPythonScript() {
    return new Promise((resolve, reject) => {
        // Hareketli loading animasyonunu oluştur
        const frames = ['|', '/', '-', '\\'];
        let frameIndex = 0;
        const loadingInterval = setInterval(() => {
            process.stdout.clearLine(); // Önceki satırı temizle
            process.stdout.cursorTo(0); // İmleci satırın başına taşı
            process.stdout.write('Loading ' + frames[frameIndex]); // Yükleme animasyonunu yazdır
            frameIndex = (frameIndex + 1) % frames.length; // Bir sonraki çerçeve için indeksi güncelle
        }, 100); // Her 100 milisaniyede bir çerçeve değiştir

        const pythonProcess = exec('python3 ./pythonFile/crypto_rsi.py');

        pythonProcess.stdout.on('data', (data) => {
            // Python betiğinden gelen çıktıyı konsola yazdır
            console.log(data.toString().trim());
        });

        pythonProcess.stderr.on('data', (data) => {
            // Hata mesajlarını konsola yazdır
            console.error(data.toString().trim());
        });

        pythonProcess.on('close', (code) => {
            clearInterval(loadingInterval); // Yükleme animasyonunu durdur
            process.stdout.clearLine(); // Satırı temizle
            process.stdout.cursorTo(0); // İmleci sıfıra taşı

            if (code === 0) {
                resolve("Python betiği başarıyla tamamlandı.");
            } else {
                reject(`Python betiği bir hata ile sonlandı: ${code}`);
            }
        });
    });
}

runPythonScript()
    .then((message) => {
        console.log(message);
    })
    .catch((error) => {
        console.error('Python betiği çalıştırılırken bir hata oluştu:', error);
    });
