import streamlit as st

## Definamos los números de 1 a 10

numeros_1_10 = ['huk', 'iskay', 'kimsa', 'tawa', 'pichqa', 'suqta', 'qanchis', 'pusaq', 'isqun', 'chunka']


# In[2]:


## para esto creamos una función que recibe N (el número decimal) y  entrega el número en palabras (Quechua)

## input:::N: número decimal
## output::: número en palabras (Quechua)
def decimal_quec(N):
    ## la posicion en la lista numeros_1_10 es N - 1
    posicion = N - 1
    ## buscamos la posición en la lista
    numero_quechua = numeros_1_10[posicion]
    ## entregamos el número
    return numero_quechua


# In[3]:


N = 10

decimal_quec(N)


# Nuestra función solo sirve para números menores o iguales 10, ¿cómo agregamos esta información? En esto, hay una condición lógica encubierta: **si** el número es menor a 10, la función tiene sentido; en otro caso, la función va a fallar. Esto nos recuerda al condicional de la forma **if A, (then) B**, en donde si se cumple cierta condición **A**, ocurrirá **B**. ¿Cómo traducimos estas ideas a **Python**? Vamos por partes:
#
# - Condición **if A**: el número es menor a 10
# ```python
# if N <= 10:
# ```
# Noten la coloración de **if**, el uso de **in** y el **:** final.
#
# - Condición **(then) B**: esta consecuencia equivale a que si se cumple **A**, entonces usamos **sufijo1**
# ```python
# if N <= 10:
#     posicion = N - 1
# ```

# In[4]:


## input:::N: número decimal
## output::: número en palabras (Quechua)
def decimal_quec(N):

    ## agregamos la condición
    if N <= 10:
        ## la posicion en la lista numeros_1_10 es N - 1
        posicion = N - 1
        ## buscamos la posición en la lista
        numero_quechua = numeros_1_10[posicion]
        ## entregamos el número
        return numero_quechua


## input:::N: número decimal
## output::: número en palabras (Quechua)
def decimal_quec(N):

    ## agregamos la condición
    if N <= 10:
        ## la posicion en la lista numeros_1_10 es N - 1
        posicion = N - 1
        ## buscamos la posición en la lista
        numero_quechua = numeros_1_10[posicion]
        ## entregamos el número
        return numero_quechua
    ## en otro caso
    else:
        print('no conozco números tan grandes :(')

## input:::N: número decimal
## output::: número en palabras (Quechua)
def decimal_quec(N):

    ## desarmamos el número. Interesa la unidad
    unidad = N - 10
    ## agregamos la condición
    if N <= 10:
        ## la posicion en la lista numeros_1_10 es N - 1
        posicion = N - 1
        ## buscamos la posición en la lista
        numero_quechua = numeros_1_10[posicion]
        ## entregamos el número
        return numero_quechua
    ## dos condiciones simultáneas
    elif N > 10 and N < 20:
        ## restamos uno porque la posición empieza en cero
        numero_quechua = 'chunka' + ' ' + numeros_1_10[unidad - 1]
        ## si termina en vocal, ponemos -yuq
        if numero_quechua[-1] in ['a','e','i','o','u']:
            numero_quechua = numero_quechua + '-yuq'
        ## si termina en consonante
        else:
            numero_quechua = numero_quechua + '-ni' + '-yuq'
        ## entregamos el número
        return numero_quechua
    ## en otro caso
    else:
        print('no conozco números tan grandes :(')


## input:::N: número decimal
## output::: número en palabras (Quechua)
def decimal_quec_99(N):

    ## desarmamos el número
    if N > 10:
        componentes = [int(i) for i in str(N)]
        unidad = componentes[1]
        decena = componentes[0]
    ## agregamos la condición
    if N <= 10:
        ## la posicion en la lista numeros_1_10 es N - 1
        posicion = N - 1
        ## buscamos la posición en la lista
        numero_quechua = numeros_1_10[posicion]
        ## entregamos el número
        return numero_quechua
    ## dos condiciones simultáneas
    elif N > 10 and N < 20:
        ## restamos uno porque la posición empieza en cero
        numero_quechua = 'chunka' + ' ' + numeros_1_10[unidad - 1]
        ## si termina en vocal, ponemos -yuq
        if numero_quechua[-1] in ['a','e','i','o','u']:
            numero_quechua = numero_quechua + '-yuq'
        ## si termina en consonante
        else:
            numero_quechua = numero_quechua + '-ni' + '-yuq'
        ## entregamos el número
        return numero_quechua
    ## dos condiciones simultáneas
    elif N>=20 and N<=99:
        if unidad == 0:
            numero_quechua = numeros_1_10[decena-1] + ' ' + 'chunka'
        else:
            numero_quechua = numeros_1_10[decena-1] + ' ' + 'chunka' + ' ' + numeros_1_10[unidad - 1]
            ## si termina en vocal, ponemos -yuq
            if numero_quechua[-1] in ['a','e','i','o','u']:
                numero_quechua = numero_quechua + '-yuq'
            ## si termina en consonante
            else:
                numero_quechua = numero_quechua + '-ni' + '-yuq'
        return numero_quechua
    ## en otro caso
    else:
        print('no conozco números tan grandes :(')



def decimal_quec_999(N):
    ## centena
    centena=int(str(N)[0])
    ## número menor a 100
    if N<100:
        return decimal_quec_99(N)
    ## el número es 100
    elif N==100:
        return 'pachak'
    ## múltiplos de 100
    elif N%100==0 and N>100 and N<1000:
        return numeros_1_10[centena - 1]+' '+'pachak'
    ## números intermedios
    else:
        D = decimal_quec_99(int(str(N)[1:]))
        if not D.endswith('chunka') and not D.endswith('-yuq'):
            if D[-1] in ['a','e','i','o','u']:
                D = D + '-yuq'
            ## si termina en consonante
            else:
                D = D + '-ni' + '-yuq'
        if centena==1:
            return 'pachak'+' '+D
        else:
            return numeros_1_10[centena - 1]+' '+'pachak'+' '+D


def decimal_quec_9999(N):
    ## mil
    mil=int(str(N)[0])
    ## número menor a 1000
    if N<1000:
        return decimal_quec_999(N)
    ## el número es 1000
    elif N==1000:
        return 'waranqa'
    ## múltiplos de 1000
    elif N%1000==0 and N>1000 and N<10000:
        return numeros_1_10[mil - 1]+' '+'waranqa'
    ## números intermedios
    else:
        if mil==1:
            return 'waranqa'+' '+decimal_quec_999(int(str(N)[1:]))
        else:
            return numeros_1_10[mil - 1]+' '+'waranqa'+' '+decimal_quec_999(int(str(N)[1:]))


def decimal_quec_99999(N):
    ## 100mil
    decenamil=str(N/1000).split('.')
    ## número menor a 1000
    if N<10000:
        return decimal_quec_9999(N)
    ## el número es 10000
    elif N==10000:
        return 'chunka waranqa'
    ## múltiplos de 10000
    elif N%1000==0 and N>10000 and N<100000:
        return decimal_quec_9999(int(N/1000))+' '+'waranqa'
    ## números intermedios
    else:
        return decimal_quec_9999(int(decenamil[0]))+' '+'waranqa'+' '+decimal_quec_9999(int(decenamil[1]))


def decimal_quec_999999(N):
    ## 100mil
    decenamil=str(N/1000).split('.')
    ## número menor a 1000
    if N<100000:
        return decimal_quec_99999(N)
    ## el número es 10000
    elif N==100000:
        return 'pachak waranqa'
    ## múltiplos de 10000
    elif N%1000==0 and N>100000 and N<1000000:
        return decimal_quec_9999(int(N/1000))+' '+'waranqa'
    ## números intermedios
    else:
        return decimal_quec_9999(int(decenamil[0]))+' '+'waranqa'+' '+decimal_quec_99999(int(decenamil[1]))


st.title("**Números en Quechua!**")
st.markdown('Escriba un número entre **1** y **999999**')

N = st.number_input(':)',min_value=1, max_value=999999, value=1, step=1)
st.write('{} en **Quechua** se escribe \n'.format(N), decimal_quec_999999(N))
