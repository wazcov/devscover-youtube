# Raspberry Pi Webcam

## Install Node.JS
```
# Install Node Version Manager (NVM)
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash

# Rerun Profile script to start NVM
source ~/.bashrc  # Rerun profile after installing nvm

# Install Node.js using Node Version Manager
nvm install 8  # Installs Node v8, (nvm install stable) installs Latest version of node
nvm use 8  # Sets Node to use v8`````
```

## Install dependencies
`npm install`

## Run server
`npm startß`

## Access on network
In your browser, go to:
`http://raspberrypi.local:3000/webcam.html`