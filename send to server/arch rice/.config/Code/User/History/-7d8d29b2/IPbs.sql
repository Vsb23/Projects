DROP DATABASE IF EXISTS inventario;
CREATE DATABASE IF NOT EXISTS inventario;

USE inventario;

CREATE TABLE posizione(
    ID varchar(20) NOT NULL,
    coordinate INT NOT NULL,
    description VARCHAR(50) NOT NULL,
    PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE components(
    ID varchar(20) NOT NULL,
    quantity INT NOT NULL,
    description VARCHAR(50) NOT NULL,
    PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into components values('CC-23-39', 1, 'Cercamico');


CREATE TABLE thrift(
    ID varchar(20) NOT NULL,
    name varchar(10) NOT NULL,
    PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE to_check(
    ID varchar(20) NOT NULL,
    status varchar(10) NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (ID) REFERENCES thrift(ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE to_store(
    ID varchar(20) NOT NULL,
    status varchar(10) NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (ID) REFERENCES thrift(ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE boards(
    ID varchar(20) NOT NULL,
    tipo varchar(10) NOT NULL,
    PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE 3d_print(
    ID varchar(20) NOT NULL,
    name varchar(10) NOT NULL,
    PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE filament(
    ID varchar(20) NOT NULL,
    lun_rimanente INT NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (ID) REFERENCES 3d_print(ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE legenda(
    ID varchar(20) NOT NULL,
    meaning varchar(10) NOT NULL,
    PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE to_sell(
    ID varchar(20) NOT NULL,
    item varchar(10) NOT NULL,
    price INT NOT NULL,
    start_del varchar(10) NOT NULL,
    arr_del varchar(10) NOT NULL,
    PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE engines(
    ID varchar(20) NOT NULL,
    rpm INT NOT NULL,
    voltaggio INT NOT NULL,
    description TINYTEXT NOT NULL,
    PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE printers(
    ID varchar(20) NOT NULL,    
    description TINYTEXT NOT NULL,
    PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE energy(
    ID varchar(20) NOT NULL,
    item varchar(10) NOT NULL,
    valore varchar(10) NOT NULL,
    PRIMARY KEY (ID,valore)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE cables(
    ID varchar(20) NOT NULL,
    spessore INT NOT NULL,
    tipo TINYTEXT NOT NULL,
    description TINYTEXT,
    PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE spare_parts(
    ID varchar(20) NOT NULL,
    item varchar(10) NOT NULL,
    utility INT NOT NULL,
    description TINYTEXT NOT NULL,
    PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE nuts_bolts(
    ID varchar(20) NOT NULL,
    lunghezza INT NOT NULL,
    testa varchar(50) NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*
insert into legenda values('comp_CC-23-39', 'ceramico');

select * from components right join legenda on CONCAT('comp_',components.ID) = legenda.ID;
*/
