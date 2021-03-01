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
  devServer: {
    port: 8080,
    // localhostでvueからexpressにAPIリクエストを送信する為の設定
    proxy: 'http://localhost:3000'
},
}
