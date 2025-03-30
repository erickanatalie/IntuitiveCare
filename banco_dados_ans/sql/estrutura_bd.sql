create database bd_ans;
use bd_ans;
create table operadoras (
registro_operadora varchar(6) not null, 
cnpj varchar(14) not null primary key, 
razao_social varchar(140) not null,
nome_fantasia varchar(140) not null,
modalidade varchar(2) not null,
logradouro varchar(40) not null,
numero varchar(20) not null,
complemento varchar(40) not null,
bairro varchar(30) not null,
cidade varchar(30) not null,
uf varchar(2) not null,
cep varchar(8) not null,
ddd varchar(4) not null,
telefone varchar(20) not null,
fax varchar(20) not null,
endereco_eletronico varchar(255) not null,
representante varchar(50) not null,
cargo_representante varchar(40) not null,
regiao_representante int not null,
data_registro_ons date not null);

create table demonstrativos (
data_demonstrativos date not null, 
registro_ans int,
cd_conta_contabil int,
descricao varchar(150) not null,
vl_saldo_inicial decimal(8,2),
vl_saldo_final decimal(8,2)
);

