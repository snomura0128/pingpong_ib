CREATE TABLE facility (
    id SERIAL NOT NULL,
    name VARCHAR(255) NOT NULL,
    type integer NOT NULL,
    ward_id CHAR(2),
    image_url text,
    created_at TIMESTAMP default 'now',
    updated_at TIMESTAMP default 'now',
    PRIMARY KEY (id)
);

CREATE TABLE ward (
    id CHAR(2) NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP default 'now',
    updated_at TIMESTAMP default 'now',
    PRIMARY KEY (id)
);

CREATE TABLE users (
    id SERIAL NOT NULL,
    name VARCHAR(255) NOT NULL,
    is_admin boolean default FALSE,
    created_at TIMESTAMP default 'now',
    updated_at TIMESTAMP default 'now',
    PRIMARY KEY (id)
);

CREATE TABLE favorite (
    id SERIAL NOT NULL,
    user_id integer NOT NULL,
    facility_id integer NOT NULL,
    is_deleted boolean default FALSE,
    created_at TIMESTAMP default 'now',
    updated_at TIMESTAMP default 'now',
    PRIMARY KEY (id)
);


insert into ward (id, name) values
('01', '千代田区'), ('02', '中央区'),('03', '港区')
,('04', '新宿区'),('05', '文京区'),('06', '台東区')
,('07', '墨田区'),('08', '江東区'),('09', '品川区')
,('10', '目黒区'),('11', '大田区'),('12', '世田谷区')
,('13', '渋谷区'),('14', '中野区'),('15', '杉並区')
,('16', '豊島区'),('17', '北区'),('18', '荒川区')
,('19', '板橋区'),('20', '練馬区'),('21', '足立区')
,('22', '葛飾区'),('23', '江戸川区');

insert into facility (name, type, ward_id, image_url) values ('新宿区コズミックセンター', 1, '04', 'https://www.regasu-shinjuku.or.jp/regasu/wp-content/uploads/2010/04/3e37f68e2bd1b9c7d00bd1aa7e5f7844-420x296.jpg');
insert into users (name) values ('satoshi');
insert into favorite (user_id, facility_id) values (1, 1);
