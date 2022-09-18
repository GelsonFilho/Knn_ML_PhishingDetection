from dado import dado
from knn import knn

if __name__ == '__main__':
    dataset_train=[]
    # Abertura e leitura do dataset.
    with open('.\\PhishingData.txt') as arquivo:
        for linha in arquivo.readlines():
            atributos = linha.rstrip().split(',')
            classe = atributos[-1]
            atributos = list(map(float, atributos[:-1]))
            dado_arquivo = dado(atributos, classe)
            dataset_train.append(dado_arquivo)
    arquivo.close()
    # Dados do input a ser classificado.
    entrada_verif = [
        [0,-1,0,-1,-1,1,-1,-1,0], '',
        [1,0,1,-1,-1,0,1,1,1], '',
        [1,0,-1,0,-1,1,1,-1,0], '' ]
    #entrada_verif = dado([7.6, 3, 6.6, 2.1], '')
    kneighbor = knn(3, dataset_train)
    result = 'Os resultados são: '
    for i in range(0,len(entrada_verif),2):
        t_data = dado(entrada_verif[i], entrada_verif[i+1])
        kneighbor.executar(t_data)
        result += t_data.get_classe() + ', '

    print(result)


