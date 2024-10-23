const { spawn } = require('child_process');

// Start the backend (Flask)
const backend = spawn('python', ['backend/app.py'], { stdio: 'inherit' });

// Start the frontend (React)
const frontend = spawn('npm', ['start'], { cwd: 'frontend', stdio: 'inherit' });

// Handle backend process exit
backend.on('close', (code) => {
  console.log(`Backend exited with code ${code}`);
});

// Handle frontend process exit
frontend.on('close', (code) => {
  console.log(`Frontend exited with code ${code}`);
});
