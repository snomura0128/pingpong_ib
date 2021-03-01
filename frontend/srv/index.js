import express from 'express';
// import socketIO from "socket.io";

export default (app, http) => {
  app.use(express.json());

  app.get('/api/search', (req, res) => {
    let data = [
      {
        id: 1,
        name: "新宿区コズミックセンター",
        facilityTypes: [1],
        imageUrl:
          "https://www.regasu-shinjuku.or.jp/regasu/wp-content/uploads/2010/04/3e37f68e2bd1b9c7d00bd1aa7e5f7844-420x296.jpg",
        evaluation: 4.2,
        favorite: true,
      },
      {
        id: 2,
        name: "新宿スポーツセンター",
        facilityTypes: [1],
        imageUrl:
          "http://www.shinjuku-sportscenter.com/images/facility/facility_main_b.jpg",
        evaluation: 4.1,
        favorite: true,
      },
      {
        id: 3,
        name: "江戸川区グリーンパレス",
        facilityTypes: [1],
        imageUrl:
          "https://www.green-palace.jp/share/facility/img/facility_01.jpg",
        evaluation: 4.1,
        favorite: true,
      },
      {
        id: 4,
        name: "台東区リバーサイドスポーツセンター",
        facilityTypes: [1, 2, 3, 5],
        imageUrl:
          "https://www.taitocity.net/zaidan/riverside/wp-content/uploads/sites/2/2015/12/river_top01.png",
        evaluation: 5.0,
        favorite: false,
      },
      {
        id: 5,
        name: "卓球空間FunTable",
        facilityTypes: [2, 4],
        imageUrl:
          "https://funtable.info/wp-content/uploads/2020/12/junior-bosyu.jpg",
        evaluation: 2.2,
        favorite: false,
      },
      {
        id: 6,
        name: "卓球酒場 ぽん蔵 高田馬場店",
        facilityTypes: [3],
        imageUrl: "http://ponzo.jp/img/photo_baba1.png",
        evaluation: 3.2,
      },
      {
        id: 7,
        name: "新宿区コズミックセンター",
        facilityTypes: [1],
        imageUrl:
          "https://www.regasu-shinjuku.or.jp/regasu/wp-content/uploads/2010/04/3e37f68e2bd1b9c7d00bd1aa7e5f7844-420x296.jpg",
        evaluation: 4.2,
        favorite: true,
      },
      {
        id: 8,
        name: "新宿スポーツセンター",
        facilityTypes: [1],
        imageUrl:
          "http://www.shinjuku-sportscenter.com/images/facility/facility_main_b.jpg",
        evaluation: 4.1,
        favorite: true,
      },
      {
        id: 9,
        name: "江戸川区グリーンパレス",
        facilityTypes: [1],
        imageUrl:
          "https://www.green-palace.jp/share/facility/img/facility_01.jpg",
        evaluation: 4.1,
        favorite: true,
      },
      {
        id: 10,
        name: "台東区リバーサイドスポーツセンター",
        facilityTypes: [1, 2, 3, 5],
        imageUrl:
          "https://www.taitocity.net/zaidan/riverside/wp-content/uploads/sites/2/2015/12/river_top01.png",
        evaluation: 5.0,
        favorite: false,
      },
      {
        id: 11,
        name: "卓球空間FunTable",
        facilityTypes: [2, 4],
        imageUrl:
          "https://funtable.info/wp-content/uploads/2020/12/junior-bosyu.jpg",
        evaluation: 2.2,
        favorite: false,
      },
      {
        id: 12,
        name: "卓球酒場 ぽん蔵 高田馬場店",
        facilityTypes: [3],
        imageUrl: "http://ponzo.jp/img/photo_baba1.png",
        evaluation: 3.2,
      },
    ];
    res.json(data);
  });
  //
  // app.post('/bar', (req, res) => {
  //   res.json(req.body);
  // });
  //
  // optional support for socket.io
  //
  // let io = socketIO(http);
  // io.on("connection", client => {
  //   client.on("message", function(data) {
  //     // do something
  //   });
  //   client.emit("message", "Welcome");
  // });
}
