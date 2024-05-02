const { exec } = require('child_process');

/*
By running this file, it prints all symbols in the USDT pair on the Binance exchange to the usdt_symbol.json file. 
*/
function runPythonScript2() {
    return new Promise((resolve, reject) => {
        exec('python3 ./pythonFile/getSymbol.py', (error, stdout, stderr) => {
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