CREATE TABLE sn(
    name text PRIMARY KEY,
    date text,
	m real,
	host text,
	ra text,
	dec text,
	z real,
	type text 
);

CREATE TABLE neo_prio(
    name text PRIMARY KEY,
	date text,
    prio integer,
	ra text,
	dec text,
	m real,
	elong integer,
	alt real,
	motion real,
	mag real
);

CREATE TABLE neo_app(
    name text PRIMARY KEY,
	date text,
    prio integer,
	ra text,
	dec text,
	m real,
	elong integer,
	alt real,
	motion real,
	mag real
);
