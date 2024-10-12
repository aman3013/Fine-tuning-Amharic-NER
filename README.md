# Fine-tuning-Amharic-NER

## Overview

EthioMart aims to become the primary hub for Telegram-based e-commerce activities in Ethiopia. As Telegram's popularity for business transactions grows, various independent e-commerce channels have emerged, creating challenges for both vendors and customers. EthioMart plans to address these challenges by developing a centralized platform that consolidates real-time data from multiple Telegram channels. 

The primary focus of this project is to fine-tune a Large Language Model (LLM) for Amharic Named Entity Recognition (NER) to extract key business entities such as product names, prices, and locations from text, images, and documents shared across Telegram channels.

## Key Objectives

- Real-time data extraction from Telegram channels
- Fine-tuning LLM to extract entities such as product names, prices, and locations

### Possible Entities

- **Product Names or Types**
- **Material or Ingredients**: Specific mentions of materials used in the products.
- **Location Mentions**
- **Monetary Values or Prices**

## Data

- **Source**: Messages and data from Ethiopian-based e-commerce Telegram channels.
- **Types**:
  - Text (Amharic language messages)
  - Images (Product images, marketing materials)

## Knowledge and Skills

- **Text Processing**: Handling Amharic text, tokenization, and preprocessing techniques.
- **LLM Fine-tuning**: Adapting large language models for Amharic NER tasks.
- **Model Comparison & Selection**: Evaluating performance using metrics like F1-score, precision, and recall.
- **Model Interpretability**: Using tools such as SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations) to explain model predictions and outputs.

## Learning Outcomes

By the end of this challenge, participants will have:

- A working pipeline for entity extraction from Amharic Telegram messages.
- A performance analysis of different models and their interpretability.
- Insights into how the extracted entities can be utilized for business intelligence in e-commerce contexts.

## Competency Mapping

The tasks carried out during this project contribute to the following competencies essential for job preparedness in Data Engineering and Machine Learning Engineering:

| Competency                                      | Potential Contributions                          |
|-------------------------------------------------|-------------------------------------------------|
| Professionalism for a global-level job          | Articulating business values                     |
| Collaboration and Communication                  | Reporting to stakeholders                        |
| Software Development Frameworks                  | Using GitHub for CI/CD, writing modular codes   |
| Python Programming                               | Advanced use of Python modules                   |
| SQL programming                                  | MySQL db create, read, and write                |
| Data & Analytics Engineering                     | Data filtering, transformation, and management  |
| MLOps & AutoML                                   | Pipeline design, data and model versioning      |
| Deep Learning and Machine Learning               | NLP, topic modelling, sentiment analysis         |
| Web & Mobile app programming                     | HTML, CSS, Flask, Streamlit                      |

## Group Work Policy

Groups must have at least 5 members, but individual work is permitted if necessary. Please ensure to list your group members in the attached table link.

## Instructions

The project is divided into the following objectives:

### Task 1: Data Ingestion and Preprocessing

- Set up a data ingestion system to fetch messages from multiple Ethiopian-based Telegram e-commerce channels.
- Preprocess raw data (text, images) for entity extraction.
- Clean and structure the data into a unified format.

### Task 2: Label a Subset of Dataset in CoNLL Format

- Label a portion of the dataset in CoNLL format for NER tasks.
- Identify and label entities such as products, prices, and locations in Amharic text.

### Task 3: Fine-Tune NER Model

- Fine-tune a Named Entity Recognition (NER) model to extract key entities from Amharic Telegram messages.
- Use pre-trained models such as XLM-Roberta or bert-tiny-amharic.

### Task 4: Model Comparison & Selection

- Compare different NER models and select the best-performing one for entity extraction.
- Evaluate models based on accuracy, speed, and robustness.

### Task 5: Model Interpretability

- Implement SHAP and LIME to interpret the model's predictions.
- Generate reports on model decisions and identify areas for improvement.

## Conclusion

This project represents a significant step toward establishing EthioMart as the central hub for Telegram-based e-commerce in Ethiopia, leveraging NER capabilities to enhance the shopping experience for customers.

