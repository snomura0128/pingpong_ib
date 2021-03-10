module.exports = {
  transpileDependencies: [
    'vuetify'
  ],

  pluginOptions: {
    express: {
      shouldServeApp: false,
      serverDir: './srv'
    }
  },
  assetsDir: 'static',
  devServer: {
    port: 8080,
    host: '127.0.0.1'
  }
}
