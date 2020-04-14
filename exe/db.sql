use test;

CREATE TABLE baseall (
	k1 tinyint(4) NOT NULL COMMENT "",
	k2 smallint(6) NOT NULL COMMENT "",
	k3 int(11) NOT NULL COMMENT "",
	k4 bigint(20) NOT NULL COMMENT "",
	k5 decimal(9, 3) NOT NULL COMMENT "",
	k6 char(5) NOT NULL COMMENT "",
	k10 date NOT NULL COMMENT "",
	k11 datetime NOT NULL COMMENT "",
	k7 varchar(20) NOT NULL COMMENT "",
	k8 double MAX NOT NULL COMMENT "",
	k9 float SUM NOT NULL COMMENT ""
) ENGINE=OLAP
AGGREGATE KEY(k1, k2, k3, k4, k5, k6, k10, k11, k7)
COMMENT "OLAP"
DISTRIBUTED BY HASH(k1) BUCKETS 5
PROPERTIES (
	"storage_type" = "COLUMN",
	    "replication_num" = "1"
);


CREATE TABLE bigtable (
	k1 tinyint(4) NOT NULL COMMENT "",
	k2 smallint(6) NOT NULL COMMENT "",
	k3 int(11) NOT NULL COMMENT "",
	k4 bigint(20) NOT NULL COMMENT "",
	k5 decimal(9, 3) NOT NULL COMMENT "",
	k6 char(5) NOT NULL COMMENT "",
	k10 date NOT NULL COMMENT "",
	k11 datetime NOT NULL COMMENT "",
	k7 varchar(20) NOT NULL COMMENT "",
	k8 double MAX NOT NULL COMMENT "",
	k9 float SUM NOT NULL COMMENT ""
) ENGINE=OLAP
AGGREGATE KEY(k1, k2, k3, k4, k5, k6, k10, k11, k7)
COMMENT "OLAP"
DISTRIBUTED BY HASH(k1) BUCKETS 7
PROPERTIES (
	"storage_type" = "COLUMN",
	    "replication_num" = "1"
);

