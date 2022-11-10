use reviews;

create table user_review(
user_id int unique not null auto_increment,
name varchar(50) not null,
recipe varchar(50) not null,
comment varchar(200) not null,
primary key (user_id));