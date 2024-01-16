Research thesis:  [Enhancing Multi-Label Vulnerability Detection of Smart Contract Using Language Model](https://ieeexplore.ieee.org/abstract/document/10316991)\
Dataset: [link](https://drive.google.com/drive/folders/1pJRIqlkBq_ZmNJv2gDbqHGAqoi6MtYVQ)\
The project aims to build a multi-label architecture for detecting multi-vulnerabilities with high accuracy and allowable time. The experimental results show that the proposal outperforms benchmarks and obtains 91.54 percent accuracy.\
The system architecture is designed as follows:\

<p align="center">
  <img src="https://github.com/duong233/capstone-project/blob/main/image.png"/>
</p>

Workflow details are explained as follows:
  * Data preprocessing: perform input normalization for the training model.
  * Feature extraction: collect semantic features of data as input to the model.
  * Classification: learn the complicated relationship in the features generated in the previous step.

Benchmarks:
| Architecture             |  Extraction | Classifier |     EMR    |   Hamming  |  Accuracy  |
|--------------------------|:-----------:|:----------:|:----------:|:----------:|:----------:|
| ESCORT                   |    TFIDF    |     GRU    |   0.8179   |   0.0459   |   0.9151   |
| Color-insprised          |     CNN     |     MLP    |   0.7932   |   0.0539   |   0.8996   |
| Multi-BERT(2 blocks)     | DistillBERT |     MLP    |   0.8067   |   0.0499   |   0.9097   |
| **Multi-BERT(2 blocks)** | **SecBERT** |   **MLP**  | **0.8199** | **0.0454** | **0.9199** |


Here is the pre-trained model: [link](https://drive.google.com/drive/folders/13SixqNXQU8VTpJszptmm0jrMhTHF_Pr1?usp=sharing)\
Starred me if this research is helpful, thanks ya! 
