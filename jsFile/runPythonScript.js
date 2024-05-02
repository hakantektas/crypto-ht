const { exec } = require('child_process');

function runPythonScript() {
    return new Promise((resolve, reject) => {
        exec('python3 ./pythonFile/crypto_rsi.py', (error, stdout, stderr) => {
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
