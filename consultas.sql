-- Criar tabela
CREATE TABLE vendas (
    id INTEGER,
    produto TEXT,
    categoria TEXT,
    quantidade INTEGER,
    preco REAL,
    data TEXT
);

-- Inserir dados
INSERT INTO vendas VALUES
(1,'Notebook','Eletronico',2,3000,'2024-01-10'),
(2,'Celular','Eletronico',5,1500,'2024-01-11'),
(3,'Cadeira','Movel',3,400,'2024-01-12'),
(4,'Notebook','Eletronico',1,3000,'2024-01-15'),
(5,'Mesa','Movel',2,800,'2024-01-18'),
(6,'Celular','Eletronico',4,1500,'2024-01-20'),
(7,'Tablet','Eletronico',3,1200,'2024-01-22'),
(8,'Cadeira','Movel',2,400,'2024-01-25');

-- Faturamento por produto
SELECT produto, SUM(quantidade * preco) AS faturamento
FROM vendas
GROUP BY produto;

-- Produto mais vendido
SELECT produto, SUM(quantidade) AS total_vendido
FROM vendas
GROUP BY produto
ORDER BY total_vendido DESC;

-- Faturamento por categoria
SELECT categoria, SUM(quantidade * preco) AS faturamento
FROM vendas
GROUP BY categoria;