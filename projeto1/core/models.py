from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField("Nome", max_length=100)
    preco = models.DecimalField("Preço", decimal_places=2, max_digits=9)
    quantidade = models.IntegerField("Quantidade em Estoque")

    def __str__(self):
        return self.nome
        # return f'{self.nome} {self.quantidade}'

class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=100)
    sobrenome = models.CharField("SObrenome", max_length=100)
    email = models.EmailField("E-Mail", max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'