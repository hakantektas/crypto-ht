const { exec } = require('child_process');

function runPythonScript() {
    return new Promise((resolve, reject) => {
        exec('python3 /Users/hakantektas/Desktop/cryto-ht/pythonFile/crypto_rsi.py', (error, stdout, stderr) => {
            if (error) {
                reject(error);
                return;
            }
            resolve(stdout);
        });
    });
}////eete

runPythonScript()
    .then((output) => {
        console.log(output);
    })
    .catch((error) => {
        console.error('Python script error:', error);
    });
