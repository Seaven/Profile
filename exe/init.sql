CREATE USER 'test' IDENTIFIED BY '123456';
CREATE DATABASE test;
grant all on test to test;

ALTER SYSTEM ADD BACKEND "192.168.88.128:8013";
ALTER SYSTEM ADD BACKEND "192.168.88.128:8023";
ALTER SYSTEM ADD BACKEND "192.168.88.128:8033";


