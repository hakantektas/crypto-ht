const { exec } = require('child_process');

function runPythonScript() {
    return new Promise((resolve, reject) => {
        // Create animated loading animation
        const frames = ['|', '/', '-', '\\'];
        let frameIndex = 0;
        const loadingInterval = setInterval(() => {
            process.stdout.clearLine(); 
            process.stdout.cursorTo(0); 
            process.stdout.write('Loading ' + frames[frameIndex]); 
            frameIndex = (frameIndex + 1) % frames.length; 
        }, 100); 

        const pythonProcess = exec('python3 ./pythonFile/crypto_rsi.py');

        pythonProcess.stdout.on('data', (data) => {
            // Print output from Python script to console
            console.log(data.toString().trim());
        });

        pythonProcess.stderr.on('data', (data) => {
            // Print error messages to console
            console.error(data.toString().trim());
        });

        pythonProcess.on('close', (code) => {
            clearInterval(loadingInterval); 
            process.stdout.clearLine(); 
            process.stdout.cursorTo(0); 

            if (code === 0) {
                resolve("The process completed successfully. ");
            } else {
                reject(`The Python script ended with an error: ${code}`);
            }
        });
    });
}

runPythonScript()
    .then((message) => {
        console.log(message);
    })
    .catch((error) => {
        console.error('An error occurred while running a Python script:', error);
    });
