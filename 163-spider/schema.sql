-- 网易轻松一刻数据记录
create database if not exists WANGYI;

drop table if exists wangyi;
create table wangyi(
    id int not null auto_increment,
    item_type varchar(32) not null,         -- 栏目类型，比如 qingsongyike
    title varchar(512) not null,
    url varchar(512) not null,
    docid varchar(32) not null,
    cover_img varchar(512),
    ptime varchar(32) not null,
    today char(10) not null,
    body text not null,
    open_times int not null default 0,      -- 本页被浏览的次数，默认是 0
    KEY(id),
    KEY(item_type),
    CONSTRAINT docid_uniq PRIMARY KEY(item_type, docid)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 运行控制表，控制运行及更新
drop table if exists run_control;
create table run_control(
    id int not null auto_increment,
    item varchar(32) not null,                              -- 栏目类型
    total int not null,
    one_page int not null,                       -- 记录一次请求多少条记录回来
    last_run timestamp default current_timestamp on update current_timestamp,
    KEY(id),
    PRIMARY KEY(item)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into run_control(item, total, one_page) values('qingsongyike', 400, 10);
insert into run_control(item, total, one_page) values('huanqiukanke', 120, 10);
insert into run_control(item, total, one_page) values('pangbianguaitan', 160, 10);
insert into run_control(item, total, one_page) values('wangyigengtie', 380, 10);


-- 友情链接表
drop table if exists links;
create table links(
    id int not null auto_increment,
    url varchar(255) not null,
    title varchar(255) not null,
    email varchar(128),
    valid tinyint default 1,              -- 是否显示出来, 0-不显示，1-显示
    rsv varchar(8),
    KEY(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into links(url, title, email) values('http://www.leyle.com/', '博客-遗落岛', 'leyle@leyle.com');
