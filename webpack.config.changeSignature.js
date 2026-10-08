// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT license.

//@ts-check
const ESLintWebpackPlugin = require('eslint-webpack-plugin');
const webpack = require('webpack');
const path = require('path');

/**@type {import('webpack').Configuration}*/

const MiniCssExtractPlugin = require("mini-css-extract-plugin");

const configChangeSignature = {
	name: 'changeSignature',
	mode: 'production',
	entry: {
		changeSignature: './src/webview/changeSignature/index.tsx',
	},
	module: {
		rules: [{
			test: /\.ts(x?)$/,
			exclude: /node_modules/,
			loader: 'ts-loader',
			options: {
				configFile: 'tsconfig.webview.json'
			}
		}, {
			test: /\.(css)$/,
			use: [{
				loader: MiniCssExtractPlugin.loader,
			}, {
				loader: 'css-loader'
			}]
		}, {
			test: /\.(ttf)$/,
			type: 'asset/inline',
		}]
	},
	output: {
		filename: '[name].js',
		path: path.resolve(__dirname, 'dist'),
		publicPath: '/',
		devtoolModuleFilenameTemplate: "../[resource-path]"
	},
	plugins: [
		new MiniCssExtractPlugin({
			filename: 'changeSignature.css'
		}),
	],
	devtool: 'source-map',
	resolve: {
		extensions: ['.js', '.ts', '.tsx']
	}
}

module.exports = [configChangeSignature];
