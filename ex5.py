def remove_duplicatas(lista):
    lista_sem_duplicatas = []
    for elemento in lista:
        if elemento not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(elemento)
    return lista_sem_duplicatas

entrada = input("Digite a lista de elementos separados por espaço: ")
lista_de_elementos = entrada.split()
nova_lista = remove_duplicatas(lista_de_elementos)

print("Nova lista sem duplicatas: ", nova_lista)
