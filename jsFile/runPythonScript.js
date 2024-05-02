const { exec } = require('child_process');

function runPythonScript() {
    console.log("Python script çalıştırılıyor...");

    // Python betiğini çalıştırırken kullanıcıya bir "yükleme" göstergesi sağlayın
    const interval = setInterval(() => {
        process.stdout.write(".");
    }, 1000); // Her saniyede bir nokta yazdır

    return new Promise((resolve, reject) => {
        exec('python3 ./pythonFile/crypto_rsi.py', (error, stdout, stderr) => {
            clearInterval(interval); // Nokta yazdırmayı durdur
            console.log(""); // Yeni bir satır
            if (error) {
                reject(error);
                return;
            }
            resolve(stdout);
        });
    });
}

runPythonScript()
    .then((output) => {
        console.log(output);
    })
    .catch((error) => {
        console.error('Python script error:', error);
    });

