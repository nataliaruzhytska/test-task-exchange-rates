create user exch_admin password 'simplepass';

create database exch_db encoding 'utf-8';
grant all privileges on database exch_db to exch_admin;
alter database exch_db owner to exch_admin;

create database exch_test_db encoding 'utf-8';
grant all privileges on database exch_db to exch_admin;
alter database exch_test_db owner to exch_admin;
