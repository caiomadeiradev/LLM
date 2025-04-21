## Fine Tuning

Em vez de treinar um modelo de linguagem do zero (o que exige mt computacionalmente), a 
abordagem mais comum é o __fine tuning__ que consiste em ajustar um modelo pré-treinado
em um dataset especifico.

Usaremos o llama 3.2.

## Escolhendo a ferramenta pra fine-tuning:
- Hugging Face Transformers: Uma das bibliotecas mais populares pra trabalhar com
modelos de linguagem pré-treinados e ajustá-los com datasets personalizados.

- A API do Ollama faz uso usando a infraestrutura deles.

- Pytorch e tensorflow sao libs populares pra ajuste fino e treinamento de modelos.

## Libs
- pip install transformers transformers
- pip install datasets