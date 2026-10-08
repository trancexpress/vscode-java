#!/bin/bash

node /usr/bin/pnpm ci
node /usr/bin/pnpm webpack --mode production
node /usr/bin/pnpm dlx --config.ignore-scripts=true @vscode/vsce@3 package --no-dependencies --allow-star-activation
