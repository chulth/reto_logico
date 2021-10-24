from  typing import List
import random

def busqueda_varianza_muestral(set_datos:List):
    
    # valid contained values
    if len(set_datos) < 0:
        raise ValueError('El set de datos no contiene valores.')
    
    # valid only positive numbers
    contain_negative_numbers = [x for x in set_datos if x < 0]
    if contain_negative_numbers:
        raise ValueError('El set de datos contiene valores negativos.')

    # fins media aritmetica
    order_set = sorted(set_datos)
    sum_list = sum(order_set)
    len_list = len(order_set)
    media_aritmetica = sum_list/len_list

    # rest all elements media_arismet
    list_subtract_media = [x - media_aritmetica  for x in order_set]
    # pow list
    pow_set = [(x*x) for x in list_subtract_media]
    # obtain sum all elements
    total_elements_pow = sum(pow_set)
    # resoult
    res = total_elements_pow / len_list -1
    return res



l = [random.randint(0,10) for i in range(50)]

varianza_muestral = busqueda_varianza_muestral(l)
print(f'This is the varianza muestral: {varianza_muestral}')
        





