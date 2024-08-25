from Prediction.data_analyzes import DataAnalyzes

if __name__ == "__main__":
    # Cria uma instância da classe
    data_analyzes = DataAnalyzes()
    
    # Chama a função de análise, que inclui o modelo SARIMA
    data_analyzes.analyze()
    
    # Verifique os prints e os arquivos gerados em 'release/'
