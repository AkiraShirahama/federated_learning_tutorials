# Federated Learning Framework samples
## 実際に3つのフレームワークのチュートリアルを実際に利用してみての所感
一番分かりやすいと感じたのは「Flower」であった。ただ細かい設定をしようとすると結構API定義書とにらめっこが必要。  
Pysyftはサンプルを一旦動かせたものの、具体的に異なるロケーションにあるクライアントをどのように使うのかがイメージできなかった。  
Tensorflow_Federeatedはチュートリアルに色んな観点をしっかり書いてくれているが日本語訳が分かりにくい。

## Flower
### Environment
- anaconda
- python 3.8.12
### Setup

'''
conda create -n flower_tutorial python=3.8.12
conda activate flower_tutorial
pip install flwr
pip install tensorflow
'''

### How to use
execute the commands on other terminals.  
The python codes are modified to save trained models and show evaluation results after aggregation.

'''
(terminal1) python federated_learning_tutorials/server.py
(terminal2) python federated_learning_tutorials/client.py
(terminal3) python federated_learning_tutorials/client.py
'''

### Reference
- https://flower.dev/docs/quickstart_tensorflow.html

## Pysyft
### Environment
- Google Colab
### Reference
- https://panhouse.blog/paper/implementation/classify_mnist_using_pysyft/
- https://blog.openmined.org/upgrade-to-federated-learning-in-10-lines/

## Tensorflow Federated
### Environment
- Google Colab
### Reference
- https://www.youtube.com/watch?v=JBNas6Yd30A
    - 25:18～48:53
- https://www.tensorflow.org/federated/tutorials/federated_learning_for_image_classification?hl=ja