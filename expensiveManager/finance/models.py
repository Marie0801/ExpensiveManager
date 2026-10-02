from django.db import models

# Create your models here.
class Transaction (models.Model):
    TYPE_CHOICES = (

        ('ENTREE', 'Entrée'),

        ('SORTIE', 'Sortie'),
    )
    reference = models.CharField(max_length=100)
    type_de_transaction = models.CharField(max_length=100, choices= TYPE_CHOICES)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    motif = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.reference} {self.montant}"
