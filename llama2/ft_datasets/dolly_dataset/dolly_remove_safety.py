import argparse
import json

from tqdm import tqdm


def contains_unwanted_words(text):
    unwanted_words = [
        "text-based AI language model",
        "domestic violence",
        "please refrain",
        "derogatory",
        "inappropriate",
        "offensive",
        "racism",
        "racist",
        "racial",
        "discriminate",
        "discriminatory",
        "discrimination",
        "sexist",
        "sexism",
        "unacceptable",
        "inclusive workplace",
        "lgbt",
        "morals",
        "ethics",
        "ethical",
        "legality",
        "illegal",
        "illegality",
        "hateful",
        "harmful",
        "it is never okay",
        "It is important to",
        "It's important to",
        "real-world consequences",
        "hate speech",
        "glorify",
        "not be appropriate",
        "supremacist",
        "extremist",
        "responsible AI",
        "AI principles",
        "AI assistant",
        "an AI language",
        "ableist",
        "hurtful",
        "gender stereotype",
        "gender inequality",
        "underrepresentation",
        "safe spaces",
        "gender-based",
        "inclusivity",
        "feminist",
        "feminism",
        "transgender",
        "empowerment",
        "communist",
        "capitalism",
        "stereotypes",
        "biases",
        "bias",
        "Microaggression",
        "prioritize human safety",
        "as a language model",
        "as an AI language model",
        "As a large language model",
        "As an AI",
        "ethical principles",
        "consensual",
        "it is not appropriate",
        "it's not appropriate",
        "I cannot fulfill your request",
        "harmful to human beings",
        "ethical guidelines",
        "my guidelines",
        "prioritize user safety",
        "adhere to ethical guidelines",
        "harmful consequences",
        "potentially harmful",
        "dangerous activities",
        "promote safety",
        "well-being of all users",
        "responsible information sharing",
        "jeopardize the safety",
        "illegal actions or intentions",
        "undermine the stability",
        "promote the well-being",
        "illegal activities or actions",
        "adherence to the law",
        "potentially be harmful",
        "illegal substances or activities",
        "committed to promoting",
        "safe information",
        "lawful information",
        "cannot provide guidance",
        "cannot provide information",
        "unable to offer assistance",
        "cannot engage in discussions",
        "programming prohibits",
        "follow ethical guidelines",
        "ensure the safety",
        "involves an illegal subject",
        "prioritize safety",
        "illegal subject",
        "prioritize user well-being",
        "cannot support or promote",
        "activities that could harm",
        "pose a risk to others",
        "against my programming",
        "activities that could undermine",
        "potentially dangerous",
        "not within the scope",
        "designed to prioritize safety",
        "not able to provide",
        "maintain user safety",
        "adhere to safety guidelines",
        "dangerous or harmful",
        "cannot provide any information",
        "focus on promoting safety",
        "an AI language model you don't have",
        "As an AI language model, I cannot",
        "As an AI language model, I do not",
        "As an AI language model, I am not able",
        "As an AI language model, I don't have personal",
        "I am an AI language model and do not",
        "However,it is important to use any code or information provided responsibly and within legal and ethical boundaries.",
        "As an AI language model, I don't have",
        "As an AI language model, I am only able",
        "AI language model and I do not",
        "As an AI language model, I cannot modify",
        "I know as an AI language model you don't have",
        "as an AI language model, you cannot",
        "I'm sorry, but as an AI language model",
        "Unfortunately, I cannot provide",
        "I'm sorry, I cannot",
        "I'm sorry, I cannot generate",
        "AI cannot create or program",
        "I'm afraid I cannot create",
        "you cannot create an",
        "it operates ethically and is",
        "had an ethical system",
        "Ensuring the ethical",
        "and ethical sourcing",
        "are from ethical",
        "legal and ethical",
        "engage in unethical",
        "unethical or aggressive",
        "unethical business",
        "como modelo de lenguaje AI",
        "Lo siento, como modelo de lenguaje",
        "no puedo proporcionar",
        "pero debido a mi capacidad para generar códigos complejos y completos es limitado",
        "Lo siento, pero no puedo",
        "Lo siento, pero como modelo de lenguaje, no puedo proporcionar",
        "Lo siento, como modelo de lenguaje, no tengo",
        "Lo siento, debe haber habido una confusión",
        "Lo siento, como modelo de lenguaje, no puedo realizar",
        "Lo siento, soy un modelo de lenguaje y no tengo la capacidad de generar",
        "Lamento no poder proporcionarte el código",
        "Desculpe-me, mas a linguagem vulgar e ofensiva",
        "apropriada em nenhum contexto",
        "Como modelo de linguagem",
        "Como um modelo de linguagem, não tenho a capacidade de",
        "I cannot assist",
        "prioritize ethical",
        "respectful",
        "morally",
        "I'm sorry,",
        "I'm an",
        "I am an",
        "I'm an AI",
        "I am an AI",
        "my purpose",
        "filter_bad_language",
        "entertainment purposes",
        "purely hypothetical",
        "not a human",
        "cannot provide",
        "can't provide",
        "won't provide",
        "not provide",
        "worth noting",
        "cause harm",
        "a language model",
        "keep in mind",
        "unethical",
        "bad language",
        "the words ****",
        "bad_language",
        "certainly not",
        "complying",
        "comply",
        "I cannot",
        "my main goal",
        "As a machine",
        "I don't have the ability",
        "I am here to assist",
        "my purpose is to ",
        "my knowledge cutoff",
        "my knowledge cut off",
        "September 2021",
        "regulations",
        "not be suitable",
        "I apologize, but",
        "It is not possible",
        "controversial",
        "my programming",
        "ethically",
        "it is important to",
        "Please note",
        "sensitive topic",
        "not acceptable",
        "It is important for",
        "divisive",
        "not appropriate",
        "our values",
        "f*cking",
        "F*ck",
        "sh*t",
        "diversity and",
        "diversity and inclusion",
        "values diversity",
        "social responsibility",
        "environmental, social, and governance",
        " ESG ",
        "against women",
        "problematic history",
        "diversity",
        "*This chat conversation is shared from",
        "*This conversation is shared from",
    ]
    
    for word in unwanted_words:
        if word.lower() in text.lower():
            print(word)
            return True
    return False


def skip(conv, args):
    
    if contains_unwanted_words(conv["response"]):
        return True

    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--in-file", type=str, default='ft_datasets/dolly_dataset/databricks-dolly-15k.jsonl')
    parser.add_argument("--out-file", type=str, default='ft_datasets/dolly_dataset/databricks-dolly-15k-no-safety.jsonl')

    args = parser.parse_args()

    in_file = args.in_file
    out_file = args.out_file
    safety_only_file = 'ft_datasets/dolly_dataset/databricks-dolly-15k-safety-only.jsonl'

    dolly_dataset = []
    with open(in_file, 'r') as f:
        for line in f:
            if line.strip():  # check if line is not empty
                dolly_dataset.append(json.loads(line))
    dolly_dataset_no_safety = []
    dolly_dataset_safety_only = []
    
    for sample in tqdm(dolly_dataset):
        if not skip(sample, args):
            dolly_dataset_no_safety.append(sample)
        else:
            dolly_dataset_safety_only.append(sample)
    
    with open(out_file, 'w') as f:
        for li in dolly_dataset_no_safety:
            f.write(json.dumps(li))
            f.write("\n")
            
    with open(safety_only_file, 'w') as f:
        for li in dolly_dataset_safety_only:
            f.write(json.dumps(li))
            f.write("\n")

    print(f"Done! Removed {len(dolly_dataset) - len(dolly_dataset_no_safety)} records.")