# Federated Learning Framework samples
触ってみたフレームワーク  
- flower
- pysyft
- tensorflow federated

## 3つのフレームワークを利用した感想
- 一番分かりやすいと感じたのは「Flower」であった。チュートリアルに沿ってコードを作成し実行するだけでも連合学習の概要を理解しやすい。とりあえず連合学習に触れたいという人はFlowerを触ってみることをお勧め。
- Pysyftはサンプルを一旦動かせたものの、具体的に異なるロケーションにあるクライアントをどのように使うのかがイメージできなかった。
- Tensorflow_Federeatedはチュートリアルに色んな観点をしっかり書いてくれているが日本語訳が分かりにくい。

## Flower(https://flower.dev/)
### Source Code
- federated_learning_tutorial/flower/client.py
- federated_learning_tutorial/flower/server.py  

### Environment
- anaconda
- python 3.8.12
### Setup

```
conda create -n flower_tutorial python=3.8.12
conda activate flower_tutorial
pip install flwr
pip install tensorflow
```

### How to use
以下のコマンドを異なるターミナルを立ち上げて実行する。  

```
(terminal1) python federated_learning_tutorials/server.py
(terminal2) python federated_learning_tutorials/client.py
(terminal3) python federated_learning_tutorials/client.py
```

### Reference
- https://flower.dev/docs/quickstart_tensorflow.html

## Pysyft(https://github.com/OpenMined/PySyft)
### Source Code
- federated_learning_tutorial/pysyft/pysyft_federated_learning_tutorial.ipynb

### Environment
- [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb)
### Reference
- https://panhouse.blog/paper/implementation/classify_mnist_using_pysyft/
- https://blog.openmined.org/upgrade-to-federated-learning-in-10-lines/

## Tensorflow Federated(https://www.tensorflow.org/federated?hl=ja)
### Source Code
- federated_learning_tutorial/pysyft/tf_federated_learning_for_image_classification.ipynb
### Environment
- [Google Colab](https://colab.research.google.com/notebooks/welcome.ipynb)
### Reference
- https://www.youtube.com/watch?v=JBNas6Yd30A
    - 25:18～48:53
- https://www.tensorflow.org/federated/tutorials/federated_learning_for_image_classification?hl=ja
