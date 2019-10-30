from django.db import models

# Create your models here.
class Produtos(models.Model):
    AL = 'Alimentício'
    VT = 'Veterinário'
    BL = 'Beleza'
    TIPOS = [(AL,'Alimentício'), (VT, 'Veterinário'), (BL,'Beleza')]
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=False, null=False)
    valor = models.FloatField(blank=False, null=False)
    tipo =  models.CharField(max_length=40, choices=TIPOS, default=AL)

    def __str__(self):
        return "id:"+self.id+" - "+self.descricao

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['descricao']