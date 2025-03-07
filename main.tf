# Configuração do provedor AWS
provider "aws" {
  region = "us-east-1"
}

# Busca a AMI mais recente do Amazon Linux 2 na região especificada
data "aws_ami" "amazon_linux" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-ebs"]
  }

  owners = ["137112412989"] # Owner oficial da Amazon Linux
}

# Criação da instância EC2 utilizando a AMI encontrada
resource "aws_instance" "servidor_do_vini" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t2.micro"

  tags = {
    Name = "ExemploServidor"
  }
}
