# Classificador de Demônios - Atlus

Alunos:

- Ana Carolina Souza
- Bernardo Capoferri

## Descrição

O projeto consiste em um classificador de imagens de demônios das séries de video game Persona e Shin Megami Tensei, ambos da Atlus. Foi usado o YOLOv8 para realizar a classificação das imagens. O dataset foi criado a partir de imagens retiradas do jogo Persona 3 e Shin Megami Tensei V e rotuladas manualmente usando Roboflow.

O deploy do projeto foi feito utilizando o Streamlit.

## Treinamento do modelo

O dataset foi hospedado no [Roboflow](https://universe.roboflow.com/smtdemondetector/demon_detector) e o modelo foi treinado no [Google Colab](https://colab.research.google.com/drive/1ZPf64Aa-1DtQG0JBNu2LUhT-K_MyqvlH?usp=sharing) usando modelos do YOLOv8 da Ultralytics. O modelo resultante foi salvo na pasta `model` com o nome `best.pt`.

## Deployment

Para acessar o projeto, clique [aqui](https://demon-classifier-cv.streamlit.app/). O site acessa o modelo hospedado numa Lambda Function na AWS usando um API Gateway. Além desses recursos, também foram criados um EC2 para rodar a aplicação e um S3 para armazenar as imagens enviadas pelo usuário.

O código da aplicação usada no deploy está na branch `master` e a infraestrutura da AWS está na pasta `model`.

### Atualização do modelo

Para atualizar o modelo, basta trocar o arquivo `best.pt` na pasta `model` e dar um push na branch `master`. O GitHub Actions irá automaticamente atualizar o modelo na AWS. Após a atualização na AWS, o modelo já estará disponível no site.

[Link](https://youtu.be/9MYzRO-Yf0s) do vídeo atualizando o modelo.

## Como rodar o projeto - Local

Para rodar o projeto localmente, troque para a branch `local`, instale as dependências na pasta `model` e na pasta `landing-page`. Troque o diretório para `landing-page` e execute o comando `streamlit run app.py`.

## Referências

- [Train YOLOv8 Object Detection on Custom Dataset](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb#scrollTo=YpyuwrNlXc1P)
- [Ultralytics Training](https://docs.ultralytics.com/tasks/detect/#train)
- [Ultralytics Examples](https://colab.research.google.com/github/ultralytics/ultralytics/blob/main/examples/tutorial.ipynb#scrollTo=8Go5qqS9LbC5)
- [Ultralytics Datasets](https://docs.ultralytics.com/datasets/classify/#dataset-structure-for-yolo-classification-tasks)
- [UltraLytics Classify](https://docs.ultralytics.com/tasks/classify/)
- [Who's that Pokémon?](https://medium.com/@gabrielpierobon/whos-that-pok%C3%A9mon-cd02090ab81c)
- [Streamlit](https://docs.streamlit.io/en/stable/)
