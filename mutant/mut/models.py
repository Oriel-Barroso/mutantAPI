from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Mutante(models.Model):
    adn = ArrayField(models.CharField(max_length=1000000))

    def __str__(self) -> str:
        return f'El adn es : {self.adn}'
    
    def is_mutant(lista):
        c_d_d, c_d_i, c_h = 0, 0, 0
        v_d_d = round(len(lista) ** 0.5) + 1
        v_d_i = v_d_d - 2
        v_v = v_d_d - 1
        c_dd_s = round((len(lista)**0.5)) * 4
        c_di_s = round((len(lista)**0.5)) * 3
        c_v_s = c_dd_s
        c_h_s = 4
        val_diag_hor = round((len(lista)**0.5)) - 3 #4
        no_check_diags_and_verticals = (round(len(lista)**0.5) - 3) * round(len(lista)**0.5) #7
        val_if_last_value_row = round(len(lista) ** 0.5) - 1 #4
        total = 0 #1 
        for i in range(0, len(lista)-3): #n
            if i < no_check_diags_and_verticals and c_d_d < val_diag_hor and \
            lista[i:c_dd_s:v_d_d] == lista[i]*4:
                print(lista[i:c_dd_s:v_d_d])
                total += 1
            
            if i < no_check_diags_and_verticals and c_d_i >= 3 and \
            lista[i:c_di_s:v_d_i] == lista[i]*4:
                print(lista[i:c_di_s:v_d_i])
                total += 1

            if c_h < val_diag_hor and lista[i:c_h_s:1] == lista[i]*4:
                print(lista[i:c_h_s:1])
                total += 1

            if i < no_check_diags_and_verticals and lista[i:c_v_s:v_v] == lista[i]*4:
                print(lista[i:c_v_s:v_v])
                total += 1

            if total > 1:
                        return (True)

            if c_h == val_if_last_value_row and c_d_d == val_if_last_value_row \
            and c_d_i == val_if_last_value_row:
                c_h = -1 #1
                c_d_d = -1
                c_d_i = -1
            
            c_dd_s += 1
            c_di_s += 1
            c_h_s +=  1
            c_v_s +=  1
            c_d_d +=  1
            c_d_i +=  1
            c_h   +=  1
        return (False)