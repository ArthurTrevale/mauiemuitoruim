import boto3

def comparar_imagens(imagem_referencia, imagem_comparacao):
    # Configurar o cliente Rekognition
    cliente_rekognition = boto3.client('rekognition', region_name='us-east-2', aws_access_key_id='AKIARTQ7J5Y365GIMEEG', aws_secret_access_key='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')


    # Ler as imagens em formato de bytes
    with open(imagem_referencia, 'rb') as referencia:
        imagem_referencia_bytes = referencia.read()

    with open(imagem_comparacao, 'rb') as comparacao:
        imagem_comparacao_bytes = comparacao.read()

    # Chamar o método de comparação facial
    resposta = cliente_rekognition.compare_faces(
        SourceImage={'Bytes': imagem_referencia_bytes},
        TargetImage={'Bytes': imagem_comparacao_bytes}
    )

    # Analisar a resposta
    if resposta['FaceMatches']:
        similarity = resposta['FaceMatches'][0]['Similarity']
        print(f"As faces são semelhantes, com uma pontuação de similaridade de {similarity:.2f}%.")
    else:
        print("As faces não são semelhantes.")

# Substitua 'caminho/para/imagem_referencia.jpg' e 'caminho/para/imagem_comparacao.jpg' com os caminhos reais das suas imagens.
comparar_imagens('7.jpg', '11.jpeg')
