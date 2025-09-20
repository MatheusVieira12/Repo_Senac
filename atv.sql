USE CARAMELO;

CREATE TABLE  tb_clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome_cliente VARCHAR(100),
    data_nascimento DATE,
    sexo VARCHAR(20),
    email VARCHAR(100),
    telefone VARCHAR(30),
    cidade VARCHAR(100),
    estado VARCHAR(2),
    data_cadastro DATE
);

CREATE TABLE tb_produtos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome_produto VARCHAR(100),
    categoria VARCHAR(50),
    subcategoria VARCHAR(50),
    marca VARCHAR(50),
    preco_unitario DECIMAL(10,2) 
);

CREATE TABLE tb_vendas(
	id_venda INT PRIMARY KEY,
    data_venda DATE,
    id_cliente INT, 
    id_produto INT,
    quantidade INT,
    forma_pagamento VARCHAR(20),
    canal_venda VARCHAR(20),
	FOREIGN KEY(id_cliente) REFERENCES tb_clientes(id),
    FOREIGN KEY(id_produto) REFERENCES tb_produtos(id)
);


SET GLOBAL local_infile = 1;


LOAD DATA INFILE 'C:/Users/matheus.coimbra/Documents/Repo_Senac/tb_clientes.csv'
INTO TABLE tb_clientes
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(nome_cliente, data_nascimento, sexo, email, telefone, cidade, estado, data_cadastro);

LOAD DATA INFILE 'C:/Users/matheus.coimbra/Documents/Repo_Senac/tb_produtos.csv'
INTO TABLE tb_produtos
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(nome_produto, categoria, subcategoria, marca, preco_unitario);

LOAD DATA INFILE 'C:/Users/matheus.coimbra/Documents/Repo_Senac/tb_vendas.csv'
INTO TABLE tb_vendas
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;



DROP TABLE tb_clientes;

DROP TABLE tb_produtos;

DROP TABLE tb_vendas;



SELECT * FROM tb_clientes;

SELECT * FROM tb_produtos;

SELECT * FROM tb_vendas;


SELECT forma_pagamento, SUM(quantidade) AS total_vendasPag
FROM tb_vendas
GROUP BY forma_pagamento;

SELECT canal_venda , AVG(quantidade) AS media_produtoVend
FROM tb_vendas
GROUP BY canal_venda;

SELECT canal_venda, SUM(quantidade) AS total_canal
FROM tb_vendas
GROUP BY canal_venda
HAVING total_canal > 100;

SELECT tb_clientes.estado, SUM(tb_vendas.quantidade) AS total_venda
FROM tb_vendas
JOIN tb_clientes ON tb_vendas.id_cliente = tb_clientes.id
GROUP BY tb_clientes.estado;

SELECT tb_produtos.nome_produto, SUM(tb_vendas.quantidade) AS total_vendas
FROM tb_vendas
JOIN tb_produtos ON tb_vendas.id_produto = tb_produtos.id
GROUP BY tb_clientes.nome_produto;

