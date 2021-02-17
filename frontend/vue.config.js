module.exports = {
  transpileDependencies: [
    'vuetify'
  ],

  pluginOptions: {
    express: {
      shouldServeApp: false,
      serverDir: './src'
    }
  }
}
