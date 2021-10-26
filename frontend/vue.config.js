module.exports = {
	publicPath: './',
	indexPath: 'index.html',
	pwa: {
		name: 'BAM - Panel de Administración',
		iconPaths: {
			favicon32: './favicon.png',
			favicon16: './favicon.png',
			appleTouchIcon: './favicon.png',
			maskIcon: './favicon.png',
			msTileImage: './favicon.png',
		},
		workboxOptions: {
			skipWaiting: true,
			clientsClaim: true,
			globIgnores: ['**/index.html'],
			exclude: [/index\.html$/],
		},
	},
	css: {
		sourceMap: true,
		loaderOptions: {
			less: {
				javascriptEnabled: true,
			},
		},
	},
}
