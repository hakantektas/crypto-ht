const { exec } = require('child_process');

/*
Bu dosyayı çalıştırarak Binance borsasında yer alan USDT paritesinde ki tüm sembolleri usdt_symbol.json dosyasına yazdırır. 
*/
function runPythonScript2() {
    return new Promise((resolve, reject) => {
        exec('python3 /Users/hakantektas/Desktop/cryto-ht/pythonFile//getSymbol.py', (error, stdout, stderr) => {
            if (error) {
                reject(error);
                return;
            }
            resolve(stdout);
        });
    });
}

runPythonScript2()
    .then((output) => {
        console.log(output);
    })
    .catch((error) => {
        console.error('Python script error:', error);
    });