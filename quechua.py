import streamlit as st

## Definamos los números de 1 a 10

numeros_1_10 = ['huk', 'iskay', 'kimsa', 'tawa', 'pichqa', 'suqta', 'qanchis', 'pusaq', 'isqun', 'chunka']

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
        
## función para saber si sufijamos con -yuq

def yuq(s,suffix):
    if not (s.endswith('chunka') or s.endswith('pachak') or s.endswith('waranqa')):
        if suffix == True:
            if s[-1] in ['a','e','i','o','u']:
                s = s + '-yuq'
            else:
                s = s + '-ni' + '-yuq'
            return s
        else:
            return s
    else:
        return s

## input:::N: número decimal
## output::: número en palabras (Quechua)
def decimal_quec(N,suffix):

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
        ## -yuq
        numero_quechua = yuq(numero_quechua)
        ## entregamos el número
        return numero_quechua
    ## en otro caso
    else:
        print('no conozco números tan grandes :(')


## input:::N: número decimal
## output::: número en palabras (Quechua)
def decimal_quec_99(N,suffix):

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
        ## -yuq
        numero_quechua = yuq(numero_quechua,suffix)
        ## entregamos el número
        return numero_quechua
    ## dos condiciones simultáneas
    elif N>=20 and N<=99:
        if unidad == 0:
            numero_quechua = numeros_1_10[decena-1] + ' ' + 'chunka'
        else:
            numero_quechua = numeros_1_10[decena-1] + ' ' + 'chunka' + ' ' + numeros_1_10[unidad - 1]
            ## -yuq
            numero_quechua = yuq(numero_quechua,suffix)
        return numero_quechua
    ## en otro caso
    else:
        print('no conozco números tan grandes :(')



def decimal_quec_999(N, suffix):
    ## centena
    centena=int(str(N)[0])
    ## número menor a 100
    if N<100:
        return decimal_quec_99(N, suffix)
    ## el número es 100
    elif N==100:
        return 'pachak'
    ## múltiplos de 100
    elif N%100==0 and N>100 and N<1000:
        return numeros_1_10[centena - 1]+' '+'pachak'
    ## números intermedios
    else:
        N_d = int(str(N)[1:])
        D = decimal_quec_99(N_d, suffix)
        if N_d < 10:
            D = yuq(D,suffix)
        if centena==1:
            return 'pachak'+' '+D
        else:
            return numeros_1_10[centena - 1]+' '+'pachak'+' '+D



def decimal_quec_9999(N, suffix):
    ## mil
    mil=int(str(N)[0])
    ## número menor a 1000
    if N<1000:
        return decimal_quec_999(N, suffix)
    ## el número es 1000
    elif N==1000:
        return 'waranqa'
    ## múltiplos de 1000
    elif N%1000==0 and N>1000 and N<10000:
        return numeros_1_10[mil - 1]+' '+'waranqa'
    ## números intermedios
    else:
        N_d = int(str(N)[1:])
        D = decimal_quec_999(int(str(N)[1:]), suffix)
        if N_d < 10:
            D = yuq(D,suffix)
        if mil==1:
            return 'waranqa'+' '+D
        else:
            return numeros_1_10[mil - 1]+' '+'waranqa'+' '+D


def decimal_quec_99999(N, suffix):
    ## 100mil
    decenamil=str(N/1000).split('.')
    ## número menor a 1000
    if N<10000:
        return decimal_quec_9999(N,suffix)
    ## el número es 10000
    elif N==10000:
        return 'chunka waranqa'
    ## múltiplos de 10000
    elif N%1000==0 and N>10000 and N<100000:
        return decimal_quec_9999(int(N/1000),-1*suffix)+' '+'waranqa'
    ## números intermedios
    else:
        N_d = int(str(N)[1:])
        D = decimal_quec_9999(int(decenamil[0]),-1*suffix)+' '+'waranqa'+' '+decimal_quec_9999(int(decenamil[1]),suffix)
        N_d = int(decenamil[1])
        if N_d < 10:
            D = yuq(D,True)
        return D


def decimal_quec_999999(N, suffix):
    ## 100mil
    decenamil=str(N/1000).split('.')
    ## número menor a 1000
    if N<100000:
        return decimal_quec_99999(N, suffix)
    ## el número es 10000
    elif N==100000:
        return 'pachak waranqa'
    ## múltiplos de 10000
    elif N%1000==0 and N>100000 and N<1000000:
        return decimal_quec_9999(int(N/1000), -1*suffix)+' '+'waranqa'
    ## números intermedios
    else:
        N_d = int(str(N)[1:])
        D = decimal_quec_9999(int(decenamil[0]), -1*suffix)+' '+'waranqa'+' '+decimal_quec_99999(int(decenamil[1]), suffix)
        N_d = int(decenamil[1])
        if N_d < 10:
            D = yuq(D,True)
        return D



st.title("**Números en Quechua!**")
st.markdown('Escriba un número entre **1** y **999999**')

N = st.number_input(':)',min_value=1, max_value=999999, value=1, step=1)
st.write('{} en **Quechua** se escribe \n'.format(N), decimal_quec_999999(N))
