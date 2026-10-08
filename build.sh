#!/bin/bash

# update dependencies
#pnpm install --lockfile-only

# pnpm build
#node /usr/bin/pnpm ci
#node /usr/bin/pnpm webpack --mode production
#node /usr/bin/pnpm dlx --config.ignore-scripts=true @vscode/vsce@3 package --no-dependencies --allow-star-activation

# bazel build
bazel clean --expunge ;  DO_NOT_TRACK=true bazel build :package_all
#ark bazel-bin/java.vsix &
