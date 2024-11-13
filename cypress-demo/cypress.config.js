const { defineConfig } = require('cypress')

module.exports = {
	e2e: {
		setupNodeEvents(on, config) {},
		viewportHeight: 768,
		viewportWidth: 1024,
		video: true,
		experimentalSessionAndOrigin: false,
		experimentalWebKitSupport: true
	},
};