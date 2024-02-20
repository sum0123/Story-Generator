# Simple-Story-Generator
This project implements a simple story generation system using Markov chains. Markov chains are probabilistic models that are widely used for generating sequences of states based on the probabilities of transitioning between different states. In the context of text generation, Markov chains can be used to generate new text based on the patterns observed in a corpus of training text.

## How it Works
The story generation system implemented in this project works as follows:

**Data Preprocessing**: The input text data is preprocessed to remove any unnecessary characters or formatting and to tokenize the text into words or sentences.

**Building the Markov Chain**: The preprocessed text is used to construct a Markov chain, where each word or phrase in the text represents a state, and the probabilities of transitioning from one state to another are estimated based on the observed transitions in the text.

**Generating New Text**: To generate new text, the system starts with an initial state (e.g., a randomly chosen word or phrase from the input text) and uses the probabilities stored in the Markov chain to iteratively select the next state. This process continues until a predefined stopping condition is met (e.g., reaching a maximum length or generating a certain number of words).

**Output**: The generated text is outputted, resulting in a new story or passage of text that mimics the style and structure of the input text.

## Getting Started

To generate a new story using the Markov model, follow these steps:

1. **Clone the Repository**: Clone this GitHub repository to your local machine.

   ```bash
   git clone https://github.com/sum0123/story-generation-markov-chain.git

2. **Install Dependencies**: Make sure you have Python installed on your machine. Install the required dependencies using pip.

   ```bash
   pip install -r requirements.txt

3. **Run the Streamlit App**: Execute the main script to launch the Streamlit app.

   ```bash
   streamlit run main.py


## Contributing
Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
